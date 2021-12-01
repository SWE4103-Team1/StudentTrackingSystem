from django.utils import timezone

import pandas as pd
import copy
import itertools
import numpy as np
from datetime import date

from datamodel.models import Student, Course, Enrolment, UploadSet
from StudentTrackingSystemApp.rankings import get_rank_by_PREREQ
from dataloader.db_enhancements import bulk_save, group_enrolments_by_student_num
from dataloader.unassigned_transfers import *
from StudentTrackingSystemApp.configfuncs import get_course_type
from audits import audit, status


class DataFileExtractor:
    _transfer_section_marker = "N/A"
    _transfer_term_marker = "0000/00"
    _transfer_grade_marker = "CR"

    @staticmethod
    def _make_course_key(course_code, course_section):
        return course_code + course_section

    @staticmethod
    def _course_to_key(course):
        return DataFileExtractor._make_course_key(course.course_code, course.section)

    @staticmethod
    def _make_student_key(student_number):
        return str(student_number)

    @staticmethod
    def _student_to_key(student):
        return DataFileExtractor._make_student_key(student.student_number)

    def __init__(self, upload_set: UploadSet = None):
        if upload_set == None:
            upload_set = UploadSet(upload_datetime=timezone.now())
            upload_set.save()

        self._upload_set = upload_set

    def uploadAllFiles(self, person_file, course_file, transfer_file):
        # read input data files
        df_person = pd.read_table(person_file, squeeze=True)
        df_course = pd.read_table(course_file, squeeze=True)
        df_enrolment = copy.deepcopy(df_course)
        df_transfer_enrolment = pd.read_table(transfer_file, squeeze=True)
        df_transfer_course = copy.deepcopy(df_transfer_enrolment)

        students = self._build_person_models(df_person, df_enrolment)
        courses = self._build_course_models(df_course)
        transfer_courses = self._build_transfer_course_models(df_transfer_course)
        del df_person
        del df_course
        del df_transfer_course

        # store created objects so creating enrolment models doesn't need to query DB
        uploaded_students = dict()
        uploaded_courses = dict()
        for s in students:
            uploaded_students[DataFileExtractor._student_to_key(s)] = s
        for c in itertools.chain(courses, transfer_courses):
            uploaded_courses[DataFileExtractor._course_to_key(c)] = c

        # build enrolment models
        enrolments = self._build_enrolment_models(
            df_enrolment, uploaded_students, uploaded_courses
        )
        transfer_enrolments = self._build_transfer_enrolment_models(
            df_transfer_enrolment, uploaded_students, uploaded_courses
        )
        del df_enrolment
        del df_transfer_enrolment
        all_enrolments = list(itertools.chain(enrolments, transfer_enrolments))

        # Calculate rank & status from student's enrolments and update the models
        grouped_enrolments = group_enrolments_by_student_num(all_enrolments)
        mapped_courses = None
        for student_num, student_enrolments in grouped_enrolments.items():
            student = uploaded_students[
                DataFileExtractor._make_student_key(student_num)
            ]
            s_audit, _, mapped_courses = audit.audit_student(
                student_num, student_enrolments, copy.deepcopy(courses), mapped_courses
            )
            student.status = status.student_status(s_audit["progress"])
            student.rank = get_rank_by_PREREQ(student_num, student_enrolments)

        # Store all models in DB. Not asyncly, sadly
        bulk_save(itertools.chain(students, courses, transfer_courses))
        Enrolment.objects.bulk_create(all_enrolments)

    def get_upload_set(self):
        return self._upload_set

    def _build_person_models(self, dfp, dfe):
        dfp.drop_duplicates(subset=["Student_ID"], keep="last", inplace=True)
        # dfe_temp: enrolment dataframe for verifying students
        dfe_temp = copy.deepcopy(dfe)
        dfe_temp.drop_duplicates(subset=["Student_ID"], keep="first", inplace=True)

        # Finding Students with enrolments
        dfp = dfp.merge(dfe_temp, on=["Student_ID"], how="right", copy=False)

        # remove_columns: a list of extra columns not needed in dfp after merge (inner join)
        remove_columns = dfe_temp.drop(columns=["Student_ID", "Program"]).columns
        del dfe_temp
        dfp.drop(remove_columns, axis=1, inplace=True)

        # Make 'Program_x' and 'Program_y'back into one column 'Program'
        dfp.drop("Program_y", axis=1, inplace=True)
        dfp.rename(columns={"Program_x": "Program"}, inplace=True)
        dfp.replace({np.NaN: None}, inplace=True)

        dfp = dfp.values.tolist()
        student_models = list(map(self._new_student_model, dfp))
        return student_models

    def _build_course_models(self, dfc):
        dfc.drop_duplicates(subset=["Course", "Section"], keep="last", inplace=True)
        dfc = dfc.values.tolist()
        course_models = list(map(self._new_course_model, dfc))
        course_models.sort(key=lambda c: c.upload_set.upload_datetime)
        return course_models

    def _build_enrolment_models(self, dfe, uploaded_students, uploaded_courses):
        dfe.drop_duplicates(
            subset=["Course", "Student_ID", "Section"], keep="last", inplace=True
        )
        dfe = dfe.values.tolist()
        enrolment_models = list()
        for e in dfe:
            e_model = self._new_enrolment_model(e, uploaded_students, uploaded_courses)
            enrolment_models.append(e_model)

        return enrolment_models

    def _build_transfer_course_models(self, dft):
        # prepare transfer input
        dft = dft.loc[:, ~dft.columns.str.contains("^Unnamed")]
        dft["Title"] = dft["Title"].str.replace("UNASSIGNED", "U/A", regex=True)
        dft["Title"] = dft["Title"].str.replace("ASSIGNED", "", regex=True)
        dft["Course"].fillna(
            get_transfer_unassigned_courses(dft["Title"]), inplace=True
        )
        dft["Title"] = fix_course_title(dft["Title"])
        dft.dropna(axis=0, how="all", inplace=True)

        # create transfer course models
        dft.drop_duplicates(subset=["Course", "Title"], keep="last", inplace=True)
        dft.dropna(axis=0, how="all", inplace=True)
        dft = dft.values.tolist()
        transfer_course_models = list(map(self._new_transfer_course, dft))
        return transfer_course_models

    def _build_transfer_enrolment_models(
        self, dft, uploaded_students, uploaded_courses
    ):
        # prepare transfer input data
        dft = dft.loc[:, ~dft.columns.str.contains("^Unnamed")]
        dft["Title"] = dft["Title"].str.replace("UNASSIGNED", "U/A", regex=True)
        dft["Course"].fillna(
            get_transfer_unassigned_courses(dft["Title"]), inplace=True
        )
        dft["Title"] = dft["Title"].str.replace("ASSIGNED", "", regex=True)
        # dft["Title"] = fix_course_title(dft["Title"])
        dft.dropna(axis=0, how="all", inplace=True)
        dft_e = copy.deepcopy(dft)

        # create transfer enrolment models
        dft_e.drop_duplicates(
            subset=["Student_ID", "Course"], keep="last", inplace=True
        )
        dft_e.dropna(axis=0, how="all", inplace=True)
        dft_e = dft_e.values.tolist()
        transfer_enrolment_models = list()
        for e in dft_e:
            e_model = self._new_transfer_enrolment_model(
                e, uploaded_students, uploaded_courses
            )
            transfer_enrolment_models.append(e_model)
        return transfer_enrolment_models

    def _new_transfer_course(self, dft):
        course = Course(
            course_code=dft[1],
            name=dft[2],
            credit_hours=dft[3],
            course_type=get_course_type(dft[1]),
            upload_set=self._upload_set,
            section=DataFileExtractor._transfer_section_marker,
        )
        return course

    def _new_course_model(self, dfc):
        course = Course(
            course_code=dfc[3],
            credit_hours=dfc[6],
            name=dfc[4],
            section=dfc[8],
            upload_set=self._upload_set,
        )
        return course

    def _new_student_model(self, dfp):
        student = Student(
            student_number=dfp[0],
            name=dfp[1],
            program=dfp[7],
            campus=dfp[8],
            start_date=date.fromisoformat(dfp[9])
            if type(dfp[9]) is str
            else timezone.now(),
            upload_set=self._upload_set,
        )
        return student

    def _new_enrolment_model(self, dfe, uploaded_students, uploaded_courses):
        student_number = dfe[0]
        course_code = dfe[3]
        course_section = dfe[8]

        enrolled_student = uploaded_students.get(
            DataFileExtractor._make_student_key(student_number)
        )
        enrolled_course = uploaded_courses.get(
            DataFileExtractor._make_course_key(course_code, course_section)
        )

        if enrolled_student is None:
            raise RuntimeError(
                "cannot create enrolment without first creating student"
                + str(student_number)
            )
        if enrolled_course is None:
            raise RuntimeError(
                "cannot create enrolment without first creating course"
                + str(course_code)
            )

        enrolment = Enrolment(
            student=enrolled_student,
            term=dfe[2],
            grade=dfe[5],
            course=enrolled_course,
            upload_set=self._upload_set,
        )
        return enrolment

    def _new_transfer_enrolment_model(self, dft_e, uploaded_students, uploaded_courses):
        student_number = dft_e[0]
        course_code = dft_e[1]

        enrolled_student = uploaded_students.get(
            DataFileExtractor._make_student_key(student_number)
        )
        enrolled_course = uploaded_courses.get(
            DataFileExtractor._make_course_key(
                course_code, DataFileExtractor._transfer_section_marker
            )
        )

        if enrolled_student is None:
            raise RuntimeError(
                "cannot create transfer enrolment without first creating student"
                + str(student_number)
            )
        if enrolled_course is None:
            raise RuntimeError(
                "cannot create transfer enrolment without first creating course"
                + str(course_code)
            )

        enrolment = Enrolment(
            student=enrolled_student,
            course=enrolled_course,
            upload_set=self._upload_set,
            term=DataFileExtractor._transfer_term_marker,
            grade=DataFileExtractor._transfer_grade_marker,
        )

        return enrolment

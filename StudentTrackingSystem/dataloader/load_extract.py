from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

import pandas as pd
import time
import copy

from datamodel.models import Student, Course, Enrolment, UploadSet


def bulk_save(models):
    with transaction.atomic():
        for model in list(models):
            model.save()


class DataFileExtractor:
    _transfer_marker = "T"

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
        self._uploaded_courses = dict()
        self._uploaded_students = dict()

    def get_upload_set(self):
        return self._upload_set

    def uploadAllFiles(self, personfile, coursefile, transferfile):
        start_person_time = time.perf_counter_ns()
        self.uploadPersonDataFile(personfile)
        end_person_time = time.perf_counter_ns()
        start_course_time = end_person_time
        self.uploadCourseDataFile(coursefile)
        end_course_time = time.perf_counter_ns()
        start_transfert_time = end_course_time
        self.uploadTransferDataFile(transferfile)
        end_transfer_time = time.perf_counter_ns()

        person_dur = end_person_time - start_person_time
        course_dur = end_course_time - start_course_time
        transfer_dur = end_transfer_time - start_transfert_time
        print(
            "person duration:",
            person_dur / 1000000,
            "course duration:",
            course_dur / 1000000,
            "transfer duration:",
            transfer_dur / 1000000,
        )

    # **Upload PersonData File : creates Student Models**
    def uploadPersonDataFile(self, personfile):
        person_start_read = time.perf_counter_ns()
        dfp = pd.read_table(personfile, header=0, squeeze=True)
        person_end_read = time.perf_counter_ns()
        person_proc_start = person_end_read
        dfp = dfp.loc[:, ~dfp.columns.str.contains("^Unnamed")]
        student_models = self.IterStudents(dfp)
        person_proc_end = time.perf_counter_ns()
        person_db_start = person_proc_end

        bulk_save(student_models)

        self._uploaded_students = {
            DataFileExtractor._student_to_key(s): s for s in student_models
        }
        person_db_end = time.perf_counter_ns()

        read_dur = person_end_read - person_start_read
        proc_dur = person_proc_end - person_proc_start
        db_dur = person_db_end - person_db_start
        print(
            "read duration:",
            read_dur / 1000000,
            "proc duration:",
            proc_dur / 1000000,
            "db duration:",
            db_dur / 1000000,
        )

    def IterStudents(self, dfp):
        dfp.drop_duplicates(subset=["Student_ID"], keep="last", inplace=True)
        dfp = dfp.values.tolist()
        studentList = list(map(self.makeStudent, dfp))
        return studentList

    def makeStudent(self, dfp):
        student = Student(
            student_number=dfp[0],
            name=dfp[1],
            program=dfp[7],
            campus=dfp[8],
            start_date=dfp[9],
            upload_set=self._upload_set,
        )
        return student

    # **Upload CourseData File, creates Course and Enrolment Models
    def uploadCourseDataFile(self, coursefile):
        print("starting course upload")
        course_start_read = time.process_time_ns()
        dfc = pd.read_table(coursefile, header=0, squeeze=True)
        course_end_read = time.process_time_ns()
        course_proc_start = course_end_read
        dfe = copy.deepcopy(dfc)
        course_models = self.IterCourses(dfc)
        course_proc_end = time.process_time_ns()
        course_db_start = course_proc_end
        print("db creating courses")
        bulk_save(course_models)
        print("done creating courses")

        course_db_end = time.process_time_ns()

        self._uploaded_courses = {
            DataFileExtractor._course_to_key(c): c for c in course_models
        }

        # enrolments
        enrol_proc_start = course_db_end
        enrolmentList = self.IterEnrolments(dfe)
        enrol_proc_end = time.process_time_ns()
        enrol_db_start = enrol_proc_end
        print("db creating enrolments")
        Enrolment.objects.bulk_create(enrolmentList)
        print("done creating enrolments")
        enrol_db_end = time.process_time_ns()

        read_dur = course_end_read - course_start_read
        course_proc_dur = course_proc_end - course_proc_start
        course_db_dur = course_db_end - course_db_start
        enrol_proc_dur = enrol_proc_end - enrol_proc_start
        enrol_db_dur = enrol_db_end - enrol_db_start
        print(
            "read duration:",
            read_dur / 1000000,
            "course proc duration:",
            course_proc_dur / 1000000,
            "courses db duration:",
            course_db_dur / 1000000,
            "enrol proc duration:",
            enrol_proc_dur / 1000000,
            "enrol db duration:",
            enrol_db_dur / 1000000,
        )

    def IterCourses(self, dfc):
        dfc.drop_duplicates(subset=["Course", "Section"], keep="last", inplace=True)
        dfc = dfc.values.tolist()
        courseList = list(map(self.makeCourse, dfc))
        return courseList

    def makeCourse(self, dfc):
        course = Course(
            course_code=dfc[3],
            credit_hours=dfc[6],
            name=dfc[4],
            section=dfc[8],
            upload_set=self._upload_set,
        )
        return course

    def IterEnrolments(self, dfe):
        dfe.drop_duplicates(
            subset=["Course", "Student_ID", "Section"], keep="last", inplace=True
        )
        dfe = dfe.values.tolist()
        enrolmentList = list(map(self.makeEnrolments, dfe))
        return enrolmentList

    def makeEnrolments(self, dfe):
        student_number = dfe[0]
        course_code = dfe[3]
        course_section = dfe[8]
        enrolment = Enrolment(
            student=self._uploaded_students[
                DataFileExtractor._make_student_key(student_number)
            ],
            term=dfe[2],
            grade=dfe[5],
            course=self._uploaded_courses[
                DataFileExtractor._make_course_key(course_code, course_section)
            ],
            upload_set=self._upload_set,
        )
        return enrolment

    # **Upload TransferDataFile,creates Enrolment Models and some etxra Courses
    def uploadTransferDataFile(self, transferfile):
        dft = pd.read_table(transferfile, header=0, squeeze=True)
        dft = dft.loc[:, ~dft.columns.str.contains("^Unnamed")]
        dft["Course"].fillna(dft["Title"], inplace=True)
        dft.dropna(axis=0, how="all", inplace=True)
        dft_e = copy.deepcopy(dft)
        transfer_course_models = self.IterTransferCourse(dft)

        bulk_save(transfer_course_models)

        transfer_enrolment_models = self.IterTransferEnrolments(dft_e)
        Enrolment.objects.bulk_create(transfer_enrolment_models)

    def IterTransferCourse(self, dft):
        dft.drop_duplicates(subset=["Course"], keep="last", inplace=True)
        dft.dropna(axis=0, how="all", inplace=True)
        dft = dft.values.tolist()
        courseList = list(map(self.makeTransferCourse, dft))
        return courseList

    def makeTransferCourse(self, dft):
        course = Course(
            course_code=dft[1],
            name=dft[2],
            credit_hours=dft[3],
            upload_set=self._upload_set,
            section=DataFileExtractor._transfer_marker,
        )
        return course

    def IterTransferEnrolments(self, dft_e):
        dft_e.drop_duplicates(
            subset=["Student_ID", "Course"], keep="last", inplace=True
        )
        dft_e.dropna(axis=0, how="all", inplace=True)
        dft_e = dft_e.values.tolist()
        enrolmentList = list(map(self.makeTransferEnrolments, dft_e))
        try:
            enrolmentList = list(filter(None, enrolmentList))
        except ObjectDoesNotExist:
            pass
        return enrolmentList

    def makeTransferEnrolments(self, dft_e):
        student_number = dft_e[0]
        course_code = dft_e[1]

        enrolled_student = self._uploaded_students.get(
            DataFileExtractor._make_student_key(student_number)
        )
        enrolled_course = self._uploaded_courses.get(
            DataFileExtractor._make_course_key(
                course_code, DataFileExtractor._transfer_marker
            )
        )

        if enrolled_student is None or enrolled_course is None:
            return None

        enrolment = Enrolment(
            student=enrolled_student,
            course=enrolled_course,
            upload_set=self._upload_set,
            term=DataFileExtractor._transfer_marker,
            grade=DataFileExtractor._transfer_marker,
        )

        return enrolment

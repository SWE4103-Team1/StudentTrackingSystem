from django.db import IntegrityError
import datetime
import copy
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from datamodel.models import Student,Course,Enrolment,UploadSet

from datamodel.models import Student, Course, Enrolment, UploadSet

import pandas as pd
from pandas.io import sql


from django.db import IntegrityError


from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

# TODO: performance improvements
# - many of the calls below can become asynchronous - simplest
# - perform batch database operations - fast & efficient
# - perform batch operations on chunks of input data, each chunk in asynchronous call - fastest


class DataFileExtractor:
    _upload_set: UploadSet = None

    def __init__(self, upload_set: UploadSet = None):
        if self._upload_set == None:
            upload_set = UploadSet(upload_datetime=timezone.now())
            upload_set.save()

        self._upload_set = upload_set

    def get_upload_set(self):
        return self._upload_set

    def uploadAllFiles(self, personfile, coursefile, transferfile):
        self.uploadPersonDataFile(personfile)
        self.uploadCourseDataFile(coursefile)
        self.uploadTransferDataFile(transferfile)

    def uploadPersonDataFile(self, personfile):
        dfp = pd.read_table(
            personfile, header=0, squeeze=True, index_col=[0]
        )  # Read PersonData.txt into DataFrame
        dfp = dfp.loc[:, ~dfp.columns.str.contains("^Unnamed")]
            return self._upload_set

    def  uploadAllFiles(personfile,coursefile,transferfile):
        with ThreadPoolExecutor(max_workers=53) as e:
            e.submit(self.uploadPersonDataFile,personfile)
            e.submit(self.uploadCourseDataFile,coursefile)
            e.submit(sel.uploadTransferDataFile,transferfile)



    #**Upload PersonData File : creates Student Models**
    def uploadPersonDataFile(self,personfile):
        dfp=pd.read_table(personfile,header=0,squeeze=True) #Read PersonData.txt into DataFrame
        dfp = dfp.loc[:, ~dfp.columns.str.contains('^Unnamed')]
        studentList= self.IterStudents(dfp)
        Student.objects.bulk_create(studentList)
    def IterStudents(self,dfp):
        dfp.drop_duplicates(subset=['Student_ID'],keep='last',inplace=True)
        dfp = dfp.values.tolist()
        studentList = []
        with ProcessPoolExecutor(max_workers=2) as exe:
            studentList = exe.map(self.makeStudent,dfp)
        try:
            studentList = list(filter(None,studentList))
        except ObjectDoesNotExist:
            pass # There are no None types
        return studentList
    def makeStudent(self,dfp):
        if Student.objects.filter(
            student_number=dfp[0]
        ).exists():
            return None
        else:
            student = Student(
                student_number=dfp[0],
                name=dfp[1],
                gender=dfp[2],
                address=dfp[3],
                email=dfp[6],
                program=dfp[7],
                campus=dfp[8],
                start_date=dfp[9],
                upload_set=self.get_upload_set()
            )
        return student


    #**Upload CourseData File, creates Course and Enrolment Models
    def uploadCourseDataFile(self,coursefile):
        dfc = pd.read_table(coursefile,header=0,squeeze=True) #Read Course Data
        dfe = copy.deepcopy(dfc)
        courseList = self.IterCourses(dfc)
        Course.objects.bulk_create(courseList)
        enrolmentList = self.IterEnrolments(dfe)
        Enrolment.objects.bulk_create(enrolmentList)
    def IterCourses(self,dfc):
        dfc.drop_duplicates(subset=['Course','Section'],keep='last',inplace=True)
        dfc = dfc.values.tolist()
        courseList =[]
        with ProcessPoolExecutor(max_workers=3) as exe:
            courseList = exe.map(self.makeCourse,dfc)
        try:
            for index, row in dfp.iterrows():
                student = Student(
                    student_number=index,
                    name=row[0],
                    gender=row[1],
                    address=row[2],
                    email=row[5],
                    program=row[6],
                    campus=row[7],
                    start_date=row[8],
                    upload_set=self.get_upload_set(),
                )
                student.save()
        except IntegrityError:
            pass

    # THIS LOOP CREATES AND POPULATES THE COURSE,and Enrolment Models
    def uploadCourseDataFile(self, coursefile):
        course_dict = {}
        enrolment_dict = {}
        dfc = pd.read_table(coursefile, header=0, squeeze=True)  # Read Course Data
        for index, row in dfc.iterrows():
            try:
                if (row[3], row[8]) in course_dict:
                    pass
                else:
                    if Course.objects.filter(
                        course_code=row[3], section=row[8]
                    ).exists():
                        pass
                    else:
                        course = Course(
                            course_code=row[3],
                            credit_hours=row[6],
                            name=row[4],
                            section=row[8],
                            upload_set=self.get_upload_set,
                        )
                        course.save()
                        course_dict.update(
                            {(course.course_code, course.section): course}
                        )
            except IntegrityError:
                pass
            try:
                if (row[0], row[3]) in enrolment_dict:
                    pass
                else:
                    if Enrolment.objects.filter(
                        student=Student.objects.filter(student_number=row[0])[0],
                        course=Course.objects.filter(
                            course_code=row[3], section=row[8]
                        )[0],
                    ).exists():
                        pass
                    else:
                        enrolment = Enrolment.objects.create(
                            student=Student.objects.filter(student_number=row[0])[0],
                            term=row[2],
                            grade=row[7],
                            course=Course.objects.filter(
                                course_code=row[3], section=row[8]
                            )[0],
                            upload_set=self.get_upload_set(),
                        )
                        enrolment_dict.update(
                            {
                                (
                                    enrolment.student.student_number,
                                    enrolment.course.course_code,
                                ): enrolment
                            }
                        )
            except IntegrityError:
                pass

    def uploadTransferDataFile(self, transferfile):
        self.upload_set.transfer_data_file = transferfile
        dft = pd.read_table(transferfile, header=0, squeeze=True)  # Read TransferData
        for index, row in dft.iterrows():
            try:
                enrolment = Enrolment(
                    student=Student.objects.get_or_create(student_number=row[0])[0],
                    course=Course.objects.filter(
                        course_code=row[1], upload_set=self.get_upload_set()
                    )[0],
                    term="Transfer",
                    grade="**",
                    upload_set=self.get_upload_set(),
                )
                enrolment.save()
            except (IntegrityError, IndexError):
                pass
            courseList = list(filter(None,courseList))
        except ObjectDoesNotExist:
            pass ## There are no None types
        return courseList
    def makeCourse(self,dfc):
        if Course.objects.filter(
            course_code=dfc[3],section=dfc[8]
        ).exists():
            return None
        else:
            course = Course(
                course_code=dfc[3],
                credit_hours=dfc[6],
                name=dfc[4],
                section=dfc[8],
                upload_set=self.get_upload_set()
            )
        return course
    def IterEnrolments(self,dfe):
        dfe.drop_duplicates(subset=['Course','Student_ID','Section'],keep='last',inplace=True)
        dfe = dfe.values.tolist()
        enrolmentList=[]
        with ProcessPoolExecutor(max_workers=4) as exe:
            enrolmentList = exe.map(self.makeEnrolments,dfe)
        try:
            enrolmentList = list(filter(None,enrolmentList))
        except ObjectDoesNotExist:
            pass ## There are no None types
        return enrolmentList
    def makeEnrolments(self,dfe):
        if Enrolment.objects.filter(
            course=Course.objects.filter(
                course_code=dfe[3],section=dfe[8]
            )[0],
            student=Student.objects.filter(
                student_number=dfe[0]
            )[0]
        ).exists():
            return None
        else:
            enrolment=Enrolment(
                student=Student.objects.filter(
                    student_number=dfe[0]
                )[0],
                term=dfe[2],
                grade=dfe[5],
                course=Course.objects.filter(
                    course_code=dfe[3],
                    section=dfe[8]
                )[0],
                upload_set=self.get_upload_set()
            )
        return enrolment




    #**Upload TransferDataFile,creates Enrolment Models and some etxra Courses
    def uploadTransferDataFile(self,transferfile):
        dft = pd.read_table(transferfile,header=0,squeeze=True)
        courseList = self.IterTransferCourse(dft)
        Course.objects.bulk_create(courseList)
        enrolmentList = self.IterTransferEnrolments(dft)
        Enrolment.objects.bulk_create(enrolmentList)
    def IterTransferCourse(self,dft):
        dft['Course'].fillna(dft['Title']+"**",inplace = True)
        dft.drop_duplicates(subset=['Course'],keep='last',inplace=True)
        dft.dropna(axis=0,how='all',inplace=True)
        dft = dft.values.tolist()
        courseList=[]
        with ProcessPoolExecutor(max_workers=1) as exe:
            courseList = exe.map(self.makeTransferCourse,dft)
        try:
            courseList = list(filter(None,courseList))
        except (ObjectDoesNotExist):
            pass ## There are no None types
        return courseList
    def makeTransferCourse(self,dft):
        if Course.objects.filter(
            course_code=dft[1],
            credit_hours=dft[3],
            upload_set=self.get_upload_set()
        ).exists():
            return None
        else:
            course=Course(
                course_code=dft[1],
                credit_hours=dft[3],
                upload_set=self.get_upload_set(),
                section="**"
            )
        return course
    def IterTransferEnrolments(self,dft):
        dft['Course'].fillna(dft['Title']+"**",inplace = True)
        dft.drop_duplicates(subset=['Student_ID','Course'],keep='last',inplace=True)
        dft.dropna(axis=0,how='all',inplace=True)
        dft = dft.values.tolist()
        enrolmentList = []
        with ProcessPoolExecutor(max_workers=2) as exe:
            enrolmentList = exe.map(self.makeTransferEnrolments,dft)
        try:
            enrolmentList = list(filter(None,enrolmentList))
        except (ObjectDoesNotExist):
            pass ## There are no None types
        return enrolmentList
    def makeTransferEnrolments(self,dft):
        if Enrolment.objects.filter(
            course=Course.objects.get(
                course_code=dft[1],section='**'
            ),
            student=Student.objects.get(student_number=dft[0]),
            upload_set=self.get_upload_set(),
            term='Transfer',grade="**"
        ).exists():
            return None
        else:
            enrolment=Enrolment(
                student=Student.objects.filter(student_number=dft[0])[0],
                course=Course.objects.filter(
                    course_code=dft[1],
                    credit_hours=dft[3]
                )[0],
                upload_set=self.get_upload_set(),term="Transfer",grade="**"
            )

        return enrolment



#**

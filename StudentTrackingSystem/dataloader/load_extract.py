from django.db import IntegrityError
import datetime
import copy
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from datamodel.models import Student, Course, Enrolment, UploadSet

import pandas as pd
from pandas.io import sql


from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor


class DataFileExtractor:
    _upload_set: UploadSet = None
    def __init__(self, upload_set: UploadSet = None):
        if upload_set == None:
            upload_set = UploadSet(upload_datetime=timezone.now())
            upload_set.save()

        self._upload_set = upload_set

    def get_upload_set(self):
            return self._upload_set

    def  uploadAllFiles(self,personfile,coursefile,transferfile):
        with ThreadPoolExecutor() as e:
            thread1 = e.submit(self.uploadPersonDataFile,personfile)
            thread2= e.submit(self.uploadCourseDataFile,coursefile)
            while not thread1.done():
                sleep(0.001)
            thread3 = e.submit(self.uploadTransferDataFile,transferfile)
            e.shutdown(wait=True)



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
        with ThreadPoolExecutor() as e:
            studentList =e.map(self.makeStudent,dfp)
            e.shutdown(wait=True)
        return studentList

    def makeStudent(self,dfp):
        student = Student(
            student_number=dfp[0],
            name=dfp[1],
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
        Course.objects.bulk_create(courseList) ## WHAT DO WE DO IF DATABSE ERROR ON SOME ROWS
        enrolmentList = self.IterEnrolments(dfe)
        Enrolment.objects.bulk_create(enrolmentList)

    def IterCourses(self,dfc):
        dfc.drop_duplicates(subset=['Course','Section'],keep='last',inplace=True) #Look into inplace True
        dfc = dfc.values.tolist()
        courseList =[]
        with ThreadPoolExecutor() as e:
            courseList = e.map(self.makeCourse,dfc)
            e.shutdown(wait=True)
        return courseList


    def makeCourse(self,dfc):
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
        with ThreadPoolExecutor() as e:
            enrolmentList = e.map(self.makeEnrolments,dfe)
            e.shutdown(wait=True)
        return enrolmentList

    def makeEnrolments(self,dfe):
        enrolment=Enrolment(
            student=Student.objects.filter(
                student_number=dfe[0],
                upload_set=self.get_upload_set()
            )[0],
            term=dfe[2],
            grade=dfe[5],
            course=Course.objects.filter(
                course_code=dfe[3],
                section=dfe[8],
                upload_set=self.get_upload_set()
            )[0],
            upload_set=self.get_upload_set()
        )
        return enrolment

    #**Upload TransferDataFile,creates Enrolment Models and some etxra Courses
    def uploadTransferDataFile(self,transferfile):
        dft = pd.read_table(transferfile,header=0,squeeze=True)
        dft = dft.loc[:, ~dft.columns.str.contains('^Unnamed')]
        dft['Course'].fillna(dft['Title'],inplace = True)
        dft.dropna(axis=0,how='all',inplace=True)
        dft_e = copy.deepcopy(dft)
        courseList = self.IterTransferCourse(dft)
        Course.objects.bulk_create(courseList)
        enrolmentList = self.IterTransferEnrolments(dft_e)

        Enrolment.objects.bulk_create(enrolmentList)

    def IterTransferCourse(self,dft):
        dft.drop_duplicates(subset=['Course'],keep='last',inplace=True)
        dft.dropna(axis=0,how='all',inplace=True)
        dft = dft.values.tolist()
        courseList=[]
        with ThreadPoolExecutor() as e:
            courseList = e.map(self.makeTransferCourse,dft)
            e.shutdown(wait=True)
        return courseList

    def makeTransferCourse(self,dft):
        course=Course(
            course_code=dft[1],
            name = dft[2],
            credit_hours=dft[3],
            upload_set=self.get_upload_set(),
            section="**"
        )
        return course

    def IterTransferEnrolments(self,dft_e):
        dft_e.drop_duplicates(subset=['Student_ID','Course'],keep='last',inplace=True)
        dft_e.dropna(axis=0,how='all',inplace=True)
        dft_e = dft_e.values.tolist()
        enrolmentList = []
        with ThreadPoolExecutor() as e:
            enrolmentList = e.map(self.makeTransferEnrolments,dft_e)
            e.shutdown(wait=True)
        try:
            enrolmentList = list(filter(None, enrolmentList))
        except ObjectDoesNotExist:
            pass
        return enrolmentList

    def makeTransferEnrolments(self,dft_e):
        if not (
            Student.objects.filter(
                student_number=dft_e[0],
                upload_set=self.get_upload_set()
                ).exists() and
            Course.objects.filter(
                course_code=dft_e[1],
                name = dft_e[2],
                credit_hours=dft_e[3],
                upload_set=self.get_upload_set(),
                section="**"
            ).exists()
        ):
            return None

        else:
            enrolment=Enrolment(
                student=Student.objects.filter(
                    student_number=dft_e[0],
                    upload_set=self.get_upload_set()
                    )[0],
                    course=Course.objects.filter(
                    course_code=dft_e[1],
                    credit_hours=dft_e[3],
                    upload_set=self.get_upload_set()
                    )[0],
                    upload_set=self.get_upload_set(),
                    term="Transfer",grade="**"
            )

        return enrolment

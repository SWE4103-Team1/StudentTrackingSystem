import os
from django.db import IntegrityError
#os.environ.setdefault('DJANGO_SETTINGS_MODULE','StudentTrackingSystem.settings')
import datetime
#os.system("python3 manage.py flush")

#import django
#from django.core.exceptions import ObjectDoesNotExist
#django.setup()

from datamodel.models import Student,Course,Enrolment,UploadSet

import pandas as pd
from pandas.io import sql


from django.core.files import File as DjangoFile

uploadSet = UploadSet(upload_date=datetime.date.today())
uploadSet.save()
def  _uploadAllFiles(personfile,coursefile,transferfile):
    uploadPersonDataFile(personfile)
    uploadCourseDataFile(coursefile)
    uploadTransferDataFile(transferfile)

def uploadPersonDataFile(personfile):
    dfp=pd.read_table(personfile,header=0,squeeze=True,index_col=[0]) #Read PersonData.txt into DataFrame
    dfp = dfp.loc[:, ~dfp.columns.str.contains('^Unnamed')]
    try:
        for index, row in dfp.iterrows():
            student = Student(student_number=index,name=row[0],gender=row[1],
            address=row[2],email=row[5],program=row[6],campus=row[7],start_date=row[8],upload_set=uploadSet)
            student.save()
    except IntegrityError:
        pass



#THIS LOOP CREATES AND POPULATES THE COURSE,and Enrolment Models
def uploadCourseDataFile(coursefile):
    course_dict = {}
    enrolment_dict={}
    dfc = pd.read_table(coursefile,header=0,squeeze=True) #Read Course Data
    for index, row in dfc.iterrows():
        try:
            if (row[3],row[8]) in course_dict :
                pass
            else:
                if Course.objects.filter(course_code=row[3],section=row[8]).exists():
                    pass
                else:
                    course = Course(course_code=row[3],
                    credit_hours=row[6],name=row[4],section=row[8],upload_set=uploadSet)
                    course.save()
                    course_dict.update({(course.course_code,course.section):course})
        except IntegrityError:
            pass
        try:
            if (row[0],row[3]) in enrolment_dict:
                pass
            else:
                if Enrolment.objects.filter(student=Student.objects.filter(student_number=row[0])[0],
                course=Course.objects.filter(course_code=row[3],section=row[8])[0]).exists():
                    pass
                else:
                    enrolment = Enrolment.objects.create(student=Student.objects.filter(student_number=row[0])[0],
                                term=row[2],grade=row[7],course=Course.objects.filter(course_code=row[3],section=row[8])[0],upload_set=uploadSet)
                    enrolment_dict.update({(enrolment.student.student_number,enrolment.course.course_code):enrolment})
        except IntegrityError:
            pass


def uploadTransferDataFile(transferfile):
    uploadSet.transfer_data_file = transferfile
    dft = pd.read_table(transferfile,header=0,squeeze=True)   #Read TransferData
    for index, row in dft.iterrows():
        try:
            enrolment = Enrolment(student=Student.objects.get_or_create(student_number=row[0])[0],course=Course.objects.filter(course_code=row[1],
                        upload_set=uploadSet)[0],term="Transfer",grade='**',upload_set=uploadSet)
            enrolment.save()
        except (IntegrityError,IndexError):
            pass



# def main():
#     personfile = open('personData.txt','r')
#     transferfile = open('transferData.txt','r')
#     coursefile = open('courseData.txt','r')
#     _uploadAllFiles(personfile,coursefile,transferfile)
# if __name__ == "__main__":
#     main()
#****************************************************************************************************************************************


#********************************************************************************************************************************************************


#****************************************************************************************************************************************************




#******************************************************************************************************************************



## Notes
#***************************************************************************************************************

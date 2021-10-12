import os
from django.db import IntegrityError
os.environ.setdefault('DJANGO_SETTINGS_MODULE','StudentTrackingSystem.settings')
os.system("python3 manage.py flush")

import django
from django.core.exceptions import ObjectDoesNotExist
django.setup()

from ben_app.models import Student,Course,Enrolment,UploadSet



import pandas as pd
from pandas.io import sql

dfp=pd.read_table('personData.txt',header=0,squeeze=True,index_col=[0]) #Read PersonData.txt into DataFrame
dfp = dfp.loc[:, ~dfp.columns.str.contains('^Unnamed')]


dfc = pd.read_table('courseData.txt',header=0,squeeze=True) #Read Course Data
dft = pd.read_table('transferData.txt',header=0,squeeze=True)   #Read TransferData


# **********I HIGHLY SUGGEST DOWNLOADING A SQLITE3 DB BROWSER TO OBSERVE DB TABLES****************************

#*************************************************************************************************************************
#***********************************************************************************************************************
uploadSet = UploadSet.objects.create(upload_date="2021-10-09",course_data_file='courseData.txt',
                        person_data_file='transferData.txt',transfer_data_file='transferData.txt')


course_dict = {}
enrolment_dict={}

#THIS LOOP CREATES AND POPULATES THE STUDENT MODEL

for index, row in dfp.iterrows():
    student = Student.objects.create(student_number=index,name=row[0],gender=row[1],
    address=row[2],email=row[5],program=row[6],campus=row[7],start_date=row[8],upload_set=uploadSet)
    student.save()


    #I CHANGED MODELS.PY star_date DATEFRAME TO CHARFRAME for my own convenience and will switch back
     #KEEP THIS IN MIND B.G



#**********************************************************************************************************************************

#THIS LOOP CREATES AND POPULATES THE COURSE,COURSE,SECTION and Enrolment Models,
for index, row in dfc.iterrows():
    try:
        if (row[3],row[8]) in course_dict :
            pass
        else:
            course = Course.objects.create(course_code=row[3],
            credit_hours=row[6],name=row[4],section=row[8],upload_set=uploadSet)
            course.save()
            course_dict.update({(course.course_code,course.section):course})

        if (row[0],row[3]) in enrolment_dict:
            pass
        else:
            enrolment = Enrolment.objects.create(student=Student.objects.filter(student_number=row[0])[0],
                        term=row[2],grade=row[7],course=course_dict.get((row[3],row[8])),upload_set=uploadSet)
            enrolment.save()
            enrolment_dict.update({(enrolment.student.student_number,enrolment.course.course_code):enrolment})
    except IntegrityError:
        pass

for index, row in dft.iterrows():
    try:
        enrolment = Enrolment.objects.create(student=Student.objects.get_or_create(student_number=row[0])[0],course=Course.objects.filter(course_code=row[1],
        upload_set=uploadSet)[0],term="Transfer",grade='**',upload_set=uploadSet)
        enrolment.save()
        # enrolment_dict.update({(enrolment.student.student_number,enrolment.course.course_code):enrolment})
    except (IntegrityError,IndexError):
        pass








#****************************************************************************************************************************************


#********************************************************************************************************************************************************


#****************************************************************************************************************************************************




#******************************************************************************************************************************



## Notes
#***************************************************************************************************************

##ONCE EXECUTED, MY CODE WILL ASK FOR USER INPUT AND ASKS YOU TO FLUSH DATABASE BEFORE RUNNING,SAY YES

#***********************************************************************************************************************
#To run the code just focuse on this file: pyton3 load_extract.py

## IF YOU CHANGE ANYTHING AT ALL IN models.py run - python3 manage.py migrate
                                                    #python3 manage.py makemigrations
                                                    #python3 manage.py migrate
## RUN those 3 commands every once in a while to make sure everything is up to date

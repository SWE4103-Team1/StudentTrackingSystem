from django.db.models.query_utils import select_related_descend
#from django.test import TestCase
from unittest import TestCase
from .models import Student, Course, Enrolment, CourseSection

from datetime import date

# sid = models.IntegerField(primary_key=True)
# name = models.CharField(max_length=70)
# gender = models.CharField(max_length=1)
# address = models.TextField(max_length=140)
# email = models.EmailField(max_length=50)
# campus = models.CharField(max_length=2)
# program = models.CharField(max_length=10)
# start_date = models.DateField(max_length=8)


class Tests(TestCase):
    def test_create_student(self):
        global student
        student = Student(
            sid=123456,
            name="john doe",
            gender="M",
            address="123 cool street",
            email="john@unb.ca",
            campus="FR",
            program="Computer Science",
            start_date=date(2020, 10, 4),
        )
        student.save()
  
    def test_create_course(self):
        course = Course(
            course_code = "SWE4103",
            credit_hours = 3,
            name = "This Class Name",
        )
        course.save()

    def test_create_courseSection(self):
        selected_course = [course for course in Course.objects.all() if course.course_code == "SWE4103"]
        print('xxxxxxxxxxxxxxxxxxxxx' + str(selected_course))
        course_section = CourseSection(
            section = "FR01B",
            course_code = selected_course[0],
        )
        course_section.save()

    def test_create_enrollment(self):  
        selected_course_section = [courseSection for courseSection in CourseSection.objects.all() if courseSection.section == "FR01B"]
        selected_student = [student for student in Student.objects.all() if student.sid == 123456]
        enrollment = Enrolment(
            sid = selected_student[0],
            course_section = selected_course_section[0],
            term = "WI2021",
            grade = "F",
        )
        enrollment.save()
        

    

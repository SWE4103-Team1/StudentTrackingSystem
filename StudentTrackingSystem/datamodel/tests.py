
'''
Author: Justen George Di Ruscio, Elliot Chin
Last Edit: Elliot Chin (6.10.2021)
'''


from django.db.models.query_utils import select_related_descend
from django.test import TestCase
# Uncomment the bottom and comment the top import to keep the database from deleting itself
#from unittest import TestCase
from .models import Student, Course, Enrolment, CourseSection
from datetime import date

def checkEmpty(self, m):
  all_entries = m.objects.all()
  self.assertFalse(not all_entries)


class Tests(TestCase):
   
    # This creates a student object
    def test_create_student(self):
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
        # This saves the student object to the database
        student.save()
  
    # This creates a course object
    def test_create_course(self):
        course = Course(
            course_code = "SWE4103",
            credit_hours = 3,
            name = "This Class Name",
        )
        # This saves the course object to the database
        course.save()

    # This creates a course section
    def test_create_courseSection(self):
        # This returns the course with the course code "SWE4103"
        selected_course = [course for course in Course.objects.all() if course.course_code == "SWE4103"]
        course_section = CourseSection(
            section = "FR01B",
            # This sets the foreign key to the course with the course code "SWE4103"
            course_code = selected_course[0],
        )
        # This saves the course_section object to the database
        course_section.save()

    # This creates a enrollment
    def test_create_enrollment(self):  
        # This returns the course section with the section name "FR01B"
        selected_course_section = [courseSection for courseSection in CourseSection.objects.all() if courseSection.section == "FR01B"]
        enrollment = Enrolment(
            # This sets the SID Foreign key to the first student in the Student DB
            sid = Student.objects.all()[0],
            # THis sets the course_section Foreign key to the section with the name "FR01B"
            course_section = selected_course_section[0],
            term = "WI2021",
            grade = "F",
        )
        # This saves the enrollment object to the database
        enrollment.save()
              
class StudentTests(TestCase):
    def test_checkEmpty_student(self):
        checkEmpty(self, Student)
        # all_entries = Student.objects.all()
        # print(all_entries)
        # self.assertFalse(not all_entries)

    def test_checkEmail_Student(self):
        all_entries = Student.objects.all()
        self.assertTrue(x for x in all_entries if x.sid == 123456)


class CourseTests(TestCase):
    def test_checkEmpty_course(self):
        checkEmpty(self, Course)
    


'''
Author: Justen George Di Ruscio, Elliot Chin, Yuzhuo Zheng
Last Edit: Yuzhuo (6.10.2021)
'''

from django.db.models.query_utils import select_related_descend
from django.test import TestCase
# Uncomment the bottom and comment the top import to keep the database from deleting itself
from unittest import TestCase
from .models import Student, Course, Enrolment, CourseSection
from datetime import date

printNo = 0


# function for debugging
def nicePrint(x):
    global printNo
    printNo += 1
    print("\n\n\n" + str(str(printNo) + " : " + str(x)) + "\n\n\n")


# Checks if the current database is empty and returns a Boolean value
def checkEmpty(self, m):
    all_entries = m.objects.all()
    return not all_entries


# It is a test suit for checking whether entries can be inserted into database successfully
class CreateTests(TestCase):

    # django test suit tests in alphabetical order, and a, b, c, d are used for reordering
    # This creates a student object
    def test_a_create_student(self):
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

        # Null-check is performed and new entities are inserted if the database is empty
        if checkEmpty(self, Student):
            # This saves the student object to the database
            student.save()

    # This creates a course object
    def test_b_create_course(self):
        course = Course(
            course_code="SWE4103",
            credit_hours=3,
            name="This Class Name",
        )
        # This saves the course object to the database
        if checkEmpty(self, Course):
            course.save()

    # This creates a course section
    def test_c_create_courseSection(self):
        # This returns the course with the course code "SWE4103"
        selected_course = [course for course in Course.objects.all() if course.course_code == "SWE4103"]
        course_section = CourseSection(
            section="FR01B",
            # This sets the foreign key to the course with the course code "SWE4103"
            course_code=selected_course[0],
        )
        # This saves the course_section object to the database
        if checkEmpty(self, CourseSection):
            course_section.save()

    # This creates a enrollment
    def test_d_create_enrollment(self):
        # This returns the course section with the section name "FR01B" and similar to student
        selected_course_section = [courseSection for courseSection in CourseSection.objects.all() if
                                   courseSection.section == "FR01B"]
        selected_student = [student for student in Student.objects.all()]

        nicePrint(selected_student)
        enrollment = Enrolment(
            # This sets the SID Foreign key to the first student in the Student DB

            sid=selected_student[0],
            # THis sets the course_section Foreign key to the section with the name "FR01B"
            course_section=selected_course_section[0],
            term="WI2021",
            grade="F",
        )
        # This saves the enrollment object to the database
        if checkEmpty(self, Enrolment):
            enrollment.save()


# It is a class for checking empty after entries are created
class EmptyTests(TestCase):
    def test_checkEmpty_student(self):
        self.assertFalse(checkEmpty(self, Student))

    def test_checkEmpty_course(self):
        self.assertFalse(checkEmpty(self, Course))

    def test_checkEmpty_course_section(self):
        self.assertFalse(checkEmpty(self, CourseSection))

    def test_checkEmpty_enrolment(self):
        self.assertFalse(checkEmpty(self, Enrolment))


# It is a class for proofreading entries in the database.
class ProofreadingTests(TestCase):
    # Check whether Jonhn's email address is "john@unb.ca"
    def test_checkEmail_Student(self):
        all_entries = Student.objects.all()
        select_student = [x for x in all_entries if x.sid == 123456]
        for x in select_student:
            self.assertEqual(x.email, "john@unb.ca")

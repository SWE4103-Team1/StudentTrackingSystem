# from django.test import TestCase
from unittest import TestCase
from .models import Student
from .models import Course
from datetime import date


def checkEmpty(self, m):
    all_entries = m.objects.all()
    self.assertFalse(not all_entries)


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



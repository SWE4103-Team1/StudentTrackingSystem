from django.test import TestCase

from ..models import Enrolment
from .test_uploadset import UploadSetTests
from .test_course import CourseTests
from .test_student import StudentTests


class EnrolmentTests(TestCase):
    def test_create_enrolment(self):
        us_tester = UploadSetTests()
        us = us_tester.test_create_null_upload_set()

        student_tester = StudentTests()
        student = student_tester.test_create_student()

        course_tester = CourseTests()
        course = course_tester.test_create_course()

        e = Enrolment(
            student=student,
            course=course,
            term="FR/2021",
            grade="B-",
            upload_set=us,
        )
        e.save()

        self.assertEqual(e.student, student)
        self.assertEqual(e.course, course)
        self.assertEqual(e.term, "FR/2021")
        self.assertEqual(e.grade, "B-")
        self.assertEqual(e.upload_set, us)

        return e

from django.test import TestCase

from ..models import Enrolment, UploadSet
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

    def test_query_enrolment_index(self):
        e = self.test_create_enrolment()

        db_enrolment = Enrolment.objects.get(
            student=e.student, course=e.course, term=e.term, grade=e.grade, upload_set=e.upload_set
        )

        # test query enrollment
        self.assertIsNot(db_enrolment)
        self.assertEquals(db_enrolment.student, e.student)
        self.assertEquals(db_enrolment.course, e.course)
        self.assertEquals(db_enrolment.term, e.term)
        self.assertEquals(db_enrolment.grade, e.grade)
        self.assertEquals(db_enrolment.upload_set, e.upload_set)

        return db_enrolment

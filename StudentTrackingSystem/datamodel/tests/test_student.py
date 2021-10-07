from django.test import TestCase

from ..models import Student
from .test_uploadset import UploadSetTests


class StudentTests(TestCase):
    def test_create_student(self):
        us_tester = UploadSetTests()
        us = us_tester.test_create_null_upload_set()

        s = Student(
            student_number=123456,
            name="John Doe",
            gender="M",
            address="123 unb lane",
            email="johndoe@unb.ca",
            campus="FR",
            program="SWE",
            start_date=us.upload_date,
            upload_set=us,
        )
        s.save()
        self.assertEqual(s.student_number, 123456)

        return s

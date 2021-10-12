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
        self.assertEqual(s.name, "John Doe")
        self.assertEqual(s.gender, "M")
        self.assertEqual(s.address, "123 unb lane")
        self.assertEqual(s.email, "johndoe@unb.ca")
        self.assertEqual(s.campus, "FR")
        self.assertEqual(s.program, "SWE")
        self.assertEqual(s.start_date, us.upload_date)
        self.assertEqual(s.upload_set, us)

        return s

    def test_query_student_index(self):
        s = self.test_create_student()

        db_student = Student.objects.get(
            student_number=s.student_number, upload_set=s.upload_set
        )

        # test query enrollment
        self.assertIsNotNone(db_student)
        self.assertEquals(db_student.name, s.name)
        self.assertEqual(db_student.gender, s.gender)
        self.assertEqual(db_student.address, s.address)
        self.assertEqual(db_student.email, s.email)
        self.assertEqual(db_student.campus, s.campus)
        self.assertEqual(db_student.program, s.program)
        self.assertEquals(db_student.upload_set, s.upload_set)

        return db_student

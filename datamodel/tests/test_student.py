from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
import copy

from ..models import Student, UploadSet
from .test_uploadset import UploadSetTests


class StudentTests(TestCase):
    def test_create_student(self, us: UploadSet = None):
        if us is None:
            us_tester = UploadSetTests()
            us = us_tester.test_create_null_upload_set()

        s = Student(
            student_number=123456,
            name="John Doe",
            campus="FR",
            program="SWE",
            start_date=us.upload_datetime,
            upload_set=us,
        )
        s.save()

        self.assertEqual(s.student_number, 123456)
        self.assertEqual(s.name, "John Doe")
        self.assertEqual(s.campus, "FR")
        self.assertEqual(s.program, "SWE")
        self.assertEqual(s.start_date, us.upload_datetime)
        self.assertEqual(s.upload_set, us)

        return s

    def test_query_student_index(self):
        s = self.test_create_student()

        db_student = Student.objects.get(
            student_number=s.student_number,
            name=s.name,
            campus=s.campus,
            program=s.program,
            start_date=s.start_date,
            upload_set=s.upload_set,
        )

        # test query enrollment
        self.assertIsNotNone(db_student)
        self.assertEquals(db_student.name, s.name)
        self.assertEqual(db_student.campus, s.campus)
        self.assertEqual(db_student.program, s.program)
        self.assertEquals(db_student.upload_set, s.upload_set)

        return db_student

    def test_repeat_student_in_upload_set(self):
        """
        Test that the same student can be uploaded from different upload
        sets, and each student can be uniquely queried by upload set
        """

        # Create two different upload sets
        us_tester = UploadSetTests()
        us1 = us_tester.test_create_empty_upload_set(
            upload_datetime=timezone.now() - timedelta(days=1)
        )
        us2 = us_tester.test_create_empty_upload_set(upload_datetime=timezone.now())

        # Create two students with same info, but different upload sets
        student_info = Student(
            student_number=123456,
            name="John Doe",
            campus="FR",
            program="SWE",
            start_date=us1.upload_datetime.date(),
        )

        s1 = copy.copy(student_info)
        s1.start_date = us1.upload_datetime.date()
        s1.upload_set = us1
        s1.save()
        self.assertEqual(s1.student_number, student_info.student_number)
        self.assertEqual(s1.name, student_info.name)
        self.assertEqual(s1.campus, student_info.campus)
        self.assertEqual(s1.program, student_info.program)
        self.assertEqual(s1.start_date, student_info.start_date)
        self.assertEqual(s1.upload_set, us1)

        s2 = copy.copy(student_info)
        s2.upload_set = us2
        s2.save()
        self.assertEqual(s2.student_number, student_info.student_number)
        self.assertEqual(s2.name, student_info.name)
        self.assertEqual(s2.campus, student_info.campus)
        self.assertEqual(s2.program, student_info.program)
        self.assertEqual(s2.start_date, student_info.start_date)
        self.assertEqual(s2.upload_set, us2)

        # Query each student with the index, which includes the upload set - the only different field
        db_s1 = Student.objects.get(
            student_number=student_info.student_number, upload_set=us1
        )
        self.assertEqual(db_s1.student_number, student_info.student_number)
        self.assertEqual(db_s1.name, student_info.name)
        self.assertEqual(db_s1.campus, student_info.campus)
        self.assertEqual(db_s1.program, student_info.program)
        self.assertEqual(db_s1.start_date, student_info.start_date)
        self.assertEqual(db_s1.upload_set, us1)

        db_s2 = Student.objects.get(
            student_number=student_info.student_number, upload_set=us2
        )
        self.assertEqual(db_s2.student_number, student_info.student_number)
        self.assertEqual(db_s2.name, student_info.name)
        self.assertEqual(db_s2.campus, student_info.campus)
        self.assertEqual(db_s2.program, student_info.program)
        self.assertEqual(db_s2.start_date, student_info.start_date)
        self.assertEqual(db_s2.upload_set, us2)

        return db_s1, db_s2

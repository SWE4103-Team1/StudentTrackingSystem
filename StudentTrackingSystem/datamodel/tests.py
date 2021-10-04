from django.test import TestCase
from .models import Student

from datetime import date


class StudentTests(TestCase):
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
        student.save()
        self.assertEqual(student.sid, 123456)
        self.assertEqual(student.name, "john doe")

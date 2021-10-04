from django.test import TestCase
from .models import Student

from datetime import date

# sid = models.IntegerField(primary_key=True)
# name = models.CharField(max_length=70)
# gender = models.CharField(max_length=1)
# address = models.TextField(max_length=140)
# email = models.EmailField(max_length=50)
# campus = models.CharField(max_length=2)
# program = models.CharField(max_length=10)
# start_date = models.DateField(max_length=8)


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
        # self.assertEqual(student.sid, 123456)

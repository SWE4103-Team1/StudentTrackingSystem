from django.test import TestCase

from ..Util.rankings import calculateRank, prereq
from datamodel.models import Enrolment, Course
from datamodel.tests.test_uploadset import UploadSetTests
from datamodel.tests.test_student import StudentTests


class RankTests(TestCase):
    def test_calculate_rank_fir(self):
        us_tester = UploadSetTests()
        student_tester = StudentTests()

        us = us_tester.test_create_null_upload_set()
        student = student_tester.test_create_student()

        for course_id in prereq:

            if prereq[course_id] != "FIR":

                c = Course(
                    course_code=course_id,
                    section="FR01B",
                    credit_hours=3,
                    name="TEST",
                    upload_set=us,
                )
                c.save()

                e = Enrolment(
                    student=student,
                    course=c,
                    term="FR/2021",
                    grade="B-",
                    upload_set=us,
                )
                e.save()

        self.assertTrue(calculateRank(student.student_number) == "FIR")

    def test_calculate_rank_jun(self):
        us_tester = UploadSetTests()
        student_tester = StudentTests()

        us = us_tester.test_create_null_upload_set()
        student = student_tester.test_create_student()

        for course_id in prereq:

            if prereq[course_id] != "JUN":
                c = Course(
                    course_code=course_id,
                    section="FR01B",
                    credit_hours=3,
                    name="TEST",
                    upload_set=us,
                )
                c.save()

                e = Enrolment(
                    student=student,
                    course=c,
                    term="FR/2021",
                    grade="B-",
                    upload_set=us,
                )
                e.save()

        self.assertTrue(calculateRank(student.student_number) == "JUN")

    def test_calculate_rank_sop(self):
        us_tester = UploadSetTests()
        student_tester = StudentTests()

        us = us_tester.test_create_null_upload_set()
        student = student_tester.test_create_student()

        for course_id in prereq:

            if prereq[course_id] != "SOP":
                c = Course(
                    course_code=course_id,
                    section="FR01B",
                    credit_hours=3,
                    name="TEST",
                    upload_set=us,
                )
                c.save()

                e = Enrolment(
                    student=student,
                    course=c,
                    term="FR/2021",
                    grade="B-",
                    upload_set=us,
                )
                e.save()

        self.assertTrue(calculateRank(student.student_number) == "SOP")

    def test_calculate_rank_sen(self):
        us_tester = UploadSetTests()
        student_tester = StudentTests()

        us = us_tester.test_create_null_upload_set()
        student = student_tester.test_create_student()

        for course_id in prereq:

            if prereq[course_id] != "SEN":
                c = Course(
                    course_code=course_id,
                    section="FR01B",
                    credit_hours=3,
                    name="TEST",
                    upload_set=us,
                )
                c.save()

                e = Enrolment(
                    student=student,
                    course=c,
                    term="FR/2021",
                    grade="B-",
                    upload_set=us,
                )
                e.save()

        self.assertTrue(calculateRank(student.student_number) == "SEN")

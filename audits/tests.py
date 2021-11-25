from django.test import TestCase

from audits.audit import audit_student
from datamodel.models import Enrolment, Course, Student
from datamodel.tests import test_student, test_uploadset
from dataloader.db_queries import bulk_save
from dataloader.tests import DataLoaderTests


class AuditTests(TestCase):
    def test_audit(self):
        # us_tester = test_uploadset.UploadSetTests()
        # student_tester = test_student.StudentTests()
        # us = us_tester.test_create_null_upload_set()
        # student = student_tester.test_create_student(us)
        # courses = [
        #     Course(
        #         course_code="CS2333",  # core
        #         section="FR01B",
        #         credit_hours=3,
        #         name="Formal Languages",
        #         upload_set=us,
        #     ),
        #     Course(
        #         course_code="SOCI3373",  # CSE
        #         section="FR01B",
        #         credit_hours=3,
        #         name="sociology",
        #         upload_set=us,
        #     ),
        #     Course(
        #         course_code="PHYS1091",  # NS
        #         section="FR01B",
        #         credit_hours=3,
        #         name="physics, yo",
        #         upload_set=us,
        #     ),
        # ]
        # bulk_save(courses)

        # def build_enrolment(course):
        #     return Enrolment(
        #         student=student, course=course, term="2020/FA", grade="A", upload_set=us
        #     )

        # enrolments = list(map(build_enrolment, courses))
        # bulk_save(enrolments)
        upload_tester = DataLoaderTests()
        upload_tester._sample_upload_set()
        print("finished upload")
        target_student = Student.objects.all()[0]
        res, codes = audit_student(target_student.student_number)
        print(res)

from django.test import TestCase

from ..models import Course
from .test_uploadset import UploadSetTests


class CourseTests(TestCase):
    def test_create_course(self):
        us_tester = UploadSetTests()
        us = us_tester.test_create_null_upload_set()

        c = Course(
            course_code="cs2333",
            section="FR01B",
            credit_hours=3,
            name="Formal Languages",
            upload_set=us,
        )
        c.save()

        self.assertEqual(c.course_code, "cs2333")
        self.assertEqual(c.section, "FR01B")
        self.assertEqual(c.credit_hours, 3)
        self.assertEqual(c.name, "Formal Languages")
        self.assertEqual(c.upload_set, us)

        return c

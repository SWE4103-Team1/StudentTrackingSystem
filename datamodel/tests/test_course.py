from django.test import TestCase

from ..models import Course
from .test_uploadset import UploadSetTests


class CourseTests(TestCase):
    def test_create_course(self):
        us_tester = UploadSetTests()
        us = us_tester.test_create_null_upload_set()

        c = Course(
            course_code="CS2333",
            section="FR01B",
            credit_hours=3,
            name="Formal Languages",
            upload_set=us,
        )
        c.save()

        self.assertEqual(c.course_code, "CS2333")
        self.assertEqual(c.section, "FR01B")
        self.assertEqual(c.credit_hours, 3)
        self.assertEqual(c.name, "Formal Languages")
        self.assertEqual(c.upload_set, us)

        return c

    def test_query_course_index(self):
        c = self.test_create_course()

        db_course = Course.objects.get(
            course_code=c.course_code, section=c.section, upload_set=c.upload_set
        )

        self.assertIsNotNone(db_course)
        self.assertEquals(db_course.course_code, c.course_code)
        self.assertEquals(db_course.section, c.section)
        self.assertEquals(db_course.credit_hours, c.credit_hours)
        self.assertEquals(db_course.name, c.name)
        self.assertEquals(db_course.upload_set, c.upload_set)

        return db_course

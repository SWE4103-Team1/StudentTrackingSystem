from django.test import TestCase
from ..models import Course
from .test_uploadset import UploadSetTests


def get_course_by_course_code(course_code):
    selected_courses = Course.objects.all().values()
    for x in selected_courses:
        # print(str(x.items()))
        if x["course_code"] == course_code:
            return x


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

        cs2333 = get_course_by_course_code("cs2333")
        self.assertDictContainsSubset(cs2333, c.__dict__)

        return c

    def test_query_course_index(self):
        c = self.test_create_course()

        db_course = get_course_by_course_code(c.course_code)
        self.assertDictContainsSubset(db_course,c.__dict__)

        return db_course

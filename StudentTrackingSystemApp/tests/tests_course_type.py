from django.test import TestCase

from datamodel.models import Enrolment

from ..configfuncs import get_course_type
from ..rankings import get_rank_by_PREREQ
from ..rankings import get_rank_by_CH

from datamodel.tests.test_student import StudentTests
from datamodel.tests.test_course import CourseTests
from datamodel.tests.test_uploadset import UploadSetTests


class CourseTypeTest(TestCase):

    # Example core courses
    core_course_list = ["SWE4103", "CS1003", "CHEM1982"]

    # Example courses that have replacment course codes (these are all core replacment courses)
    replacement_course_list = ["ENGG4000", "ME3232", "STAT1793"]

    # Example courses that are in the exceptions list
    exception_course_list = ["CHEM1012", "PHYS1061"]

    def test_get_core_course_type(self):
        for course in self.core_course_list:
            self.assertEqual(get_course_type(course), "CORE")

    def test_get_replacement_course_type(self):
        for course in self.replacement_course_list:
            self.assertEqual(get_course_type(course), "CORE")

    def test_get_exception_course_type(self):
        for course in self.exception_course_list:
            self.assertEqual(get_course_type(course), None)

    # test for courses that are both in valid-tags and in the exceptions page
    def test_get_different_course_type(self):
        course = "ENGL1103"
        self.assertEqual(get_course_type(course), "CSE-OPEN")
        course = "ENVS2003"
        self.assertEqual(get_course_type(course), "CSE-ITS")

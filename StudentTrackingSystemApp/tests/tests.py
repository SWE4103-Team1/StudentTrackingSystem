from django.test import TestCase

from ..configfuncs import get_course_type
class CourseTypeTest(TestCase):

    # Example core courses
    core_course_list = ["SWE4103", "CS1003", "CHEM1982"]
    
    # Example courses that have replacment course codes (these are all core replacment courses)
    replacement_course_list = ["ENGG4000", "ME3232", "STAT1793"] 

    # Example courses that are in the exceptions list
    exception_course_list = ["CHEM1012", "PHYS1061", "ENGL1103"]

    def test_get_core_course_type(self):
        for course in self.core_course_list:
            self.assertEqual(get_course_type(course), 'CORE')

    def test_get_replacement_course_type(self):
        for course in self.replacement_course_list:
            self.assertEqual(get_course_type(course), 'CORE')

    def test_get_exception_course_type(self):
        for course in self.exception_course_list:
            self.assertEqual(get_course_type(course), None)
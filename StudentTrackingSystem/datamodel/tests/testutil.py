# from django.test import TestCase
#
# from ..models import Course
# from .test_uploadset import UploadSetTests
#
#
# class CourseZTests(TestCase):
#     def test_z_create_course(self):
#         us_tester = UploadSetTests()
#         us = us_tester.test_create_null_upload_set()
#
#         c = Course(
#             course_code="cs2353",
#             section="FR01C",
#             credit_hours=5,
#             name="INFormal Languages",
#             upload_set=us,
#         )
#         c.save()
#         #
#         # self.assertEqual(c.course_code, "cs2353")
#         # self.assertEqual(c.section, "FR01B")
#         # self.assertEqual(c.credit_hours, 3)
#         # self.assertEqual(c.name, "Formal Languages")
#         self.assertEqual(c.upload_set, us)
#
#         return c
#
#     def test_z_query_course_index(self):
#         c = self.test_z_create_course()
#
#         db_course = Course.objects.get(
#             course_code=c.course_code, section=c.section, upload_set=c.upload_set
#         )
#
#         self.assertIsNotNone(db_course)
#         selected_data = Course.objects.all().values()
#
#         for x in selected_data:
#             print(str(x)+"\n\n\n")
#         return db_course

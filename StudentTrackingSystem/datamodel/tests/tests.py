# from django.test import TestCase
# from unittest import TestCase
# from ..models import Student, Course, Enrolment, CourseSection

# from datetime import date


# def checkEmpty(self, m):
#     all_entries = m.objects.all()
#     self.assertFalse(not all_entries)


# class Tests(TestCase):
#     def test_create_student(self):
#         global student
#         student = Student(
#             sid=123456,
#             name="john doe",
#             gender="M",
#             address="123 cool street",
#             email="john@unb.ca",
#             campus="FR",
#             program="Computer Science",
#             start_date=date(2020, 10, 4),
#         )
#         student.save()

#     def test_create_course(self):
#         course = Course(
#             course_code="SWE4103",
#             credit_hours=3,
#             name="This Class Name",
#         )
#         course.save()

#     def test_create_courseSection(self):
#         selected_course = [
#             course for course in Course.objects.all() if course.course_code == "SWE4103"
#         ]
#         print("xxxxxxxxxxxxxxxxxxxxx" + str(selected_course))
#         course_section = CourseSection(
#             section="FR01B",
#             course_code=selected_course[0],
#         )
#         course_section.save()

#     def test_create_enrollment(self):
#         selected_course_section = [
#             courseSection
#             for courseSection in CourseSection.objects.all()
#             if courseSection.section == "FR01B"
#         ]
#         selected_student = [
#             student for student in Student.objects.all() if student.sid == 123456
#         ]
#         enrollment = Enrolment(
#             sid=selected_student[0],
#             course_section=selected_course_section[0],
#             term="WI2021",
#             grade="F",
#         )
#         enrollment.save()


# class StudentTests(TestCase):
#     def test_checkEmpty_student(self):
#         checkEmpty(self, Student)
#         # all_entries = Student.objects.all()
#         # print(all_entries)
#         # self.assertFalse(not all_entries)

#     def test_checkEmail_Student(self):
#         all_entries = Student.objects.all()
#         self.assertTrue(x for x in all_entries if x.sid == 123456)


# class CourseTests(TestCase):
#     def test_checkEmpty_course(self):
#         checkEmpty(self, Course)

from django.db import models
from models import Course
from models import Enrolment
from models import Student


class CourseManager(Course):
    def create_course(self, course_code: int, section: str, credit_hours: int, name: str):
        self.course_code = course_code
        self.section = section
        self.credit_hours = credit_hours
        self.name = name
        return Course(course_code=course_code, section=section, credit_hours=credit_hours, name=name)


class Enrolment(Enrolment):
    def creat_enrolment(self, student: Student, course: Course, grade: str, term: str):
        self.sid = student.sid
        self.course_code = course.course_code
        self.section = course.section
        self.grade = grade
        self.term = term
        return Enrolment(sid=self.sid, course_code=self.course_code, section=self.section, term=term)

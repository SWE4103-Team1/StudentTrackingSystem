from django.db import models
from models import Course
from models import Enrolment
from models import Student

from StudentTrackingSystem.StudentTrackingSystemApp.models import Student

class StudentManager(Student):

    def create_student(self, sid:int, name:str, gender:chr, address:str,email:str,campus:str, program:str, start_date:str):
        error = "Invalid entry at {}"
        if not sid:
            raise ValueError(error.format("Student ID"))

        if not name:
            raise ValueError(error.format("Full Name"))

        if not gender:
            raise ValueError(error.format("Gender"))

        if not address:
            raise ValueError(error.format("Address"))

        if not email:
            raise ValueError(error.format("Email Address"))

        if not campus:
            raise ValueError(error.format("Campus"))

        if not program:
            raise ValueError(error.format("Program"))

        if not start_date:
            raise ValueError(error.format("Start Date"))

        return Student(sid=sid, name=name, gender=gender, address=address, email=email, campus=campus, program = program, start_date = start_date)
        
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

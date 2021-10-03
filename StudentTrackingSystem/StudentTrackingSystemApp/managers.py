from django.db import models
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
        



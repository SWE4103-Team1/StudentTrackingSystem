from django.db import models


class Student(models.Model):
    sid = models.IntegerField(max_length=8, primary_key=True)
    name = models.CharField(max_length=70)
    gender = models.CharField(max_length=1)
    address = models.TextField(max_length=140)
    email = models.EmailField(max_length=50)
    campus = models.CharField(max_length=2)
    program = models.CharField(max_length=10)
    start_date = models.DateField(max_length=8)


    def __str__(self):
        return self.sid


class Course(models.Model):
    course_code = models.CharField(max_length=20, primary_key=True)
    section = models.CharField(max_length=10, primary_key=True)
    credit_hours = models.IntegerField()
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.course_code


class Enrolment(models.Model):
    sid = models.ForeignKey(Student.sid, primary_key=True)
    course_code = models.ForeignKey(Course.course_code, primary_key=True)
    section = models.ForeignKey(Course.section, primary_key=True)
    grade = models.CharField(max_length=5)
    term = models.CharField(max_length=10)

    def __str__(self):
        return self.sid


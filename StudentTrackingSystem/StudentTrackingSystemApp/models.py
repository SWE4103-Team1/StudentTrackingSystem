from django.db import models


class Course(models.Model):
    course_code = models.CharField(max_length=20, primary_key=True)
    section = models.CharField(max_length=10, primary_key=True)
    credit_hours = models.IntegerField()
    name = models.CharField(max_length=50)


class Enrolment(models.Model):
    sid = models.ForeignKey(Student.sid, primary_key=True)
    course_code = models.ForeignKey(Course.course_code, primary_key=True)
    section = models.ForeignKey(Course.section, primary_key=True)
    grade = models.CharField(max_length=5)
    term = models.CharField(max_length=10)

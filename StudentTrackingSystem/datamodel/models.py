from django.db import models


class Student(models.Model):
    sid = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=70)
    gender = models.CharField(max_length=1)
    address = models.TextField(max_length=140)
    email = models.EmailField(max_length=50)
    campus = models.CharField(max_length=2)
    program = models.CharField(max_length=10)
    start_date = models.DateField(max_length=8)

    def __str__(self):
        return f"sid: {self.sid}, name: {self.name}, gender: {self.gender}, address: {self.address}, email: {self.email}"


class Course(models.Model):
    course_code = models.CharField(max_length=20, primary_key=True)
    credit_hours = models.IntegerField()
    name = models.CharField(max_length=50)


class CourseSection(models.Model):
    section = models.CharField(max_length=10, primary_key=True)
    course_code = models.ForeignKey(Course, on_delete=models.CASCADE)


class Enrolment(models.Model):
    sid = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_section = models.ForeignKey(CourseSection, on_delete=models.CASCADE)
    term = models.CharField(max_length=10)
    grade = models.CharField(max_length=5)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["sid", "course_section"], name="unique enrolment key"
            )
        ]

    def __str__(self):
        return f"Enrolment: {self.id} (Student: {self.sid}) (Course Section: {self.section})"

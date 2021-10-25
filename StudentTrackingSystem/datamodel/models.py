from django.db import models


class UploadSet(models.Model):
    upload_datetime = models.DateTimeField(primary_key=True)
    # ensure nefarious scripts aren't uploaded
    person_data_file = models.FileField(
        upload_to="uploads/", blank=True, null=True)
    course_data_file = models.FileField(
        upload_to="uploads/", blank=True, null=True)
    transfer_data_file = models.FileField(
        upload_to="uploads/", blank=True, null=True)


class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    student_number = models.IntegerField()
    name = models.TextField(max_length=70)
    email = models.EmailField(max_length=50)
    campus = models.CharField(max_length=2)
    program = models.CharField(max_length=10)
    start_date = models.DateField(max_length=8)
    upload_set = models.ForeignKey(UploadSet, on_delete=models.CASCADE)

    class Meta:
        _index_fields = ["student_number", "upload_set"]
        indexes = [
            models.Index(fields=_index_fields, name="student_index"),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=_index_fields,
                name="unique student index constraint",
            )
        ]

    def __str__(self):
        return f"sid: {self.id}, name: {self.name}, gender: {self.gender}, address: {self.address}, email: {self.email}"


class Course(models.Model):
    id = models.BigAutoField(primary_key=True)
    course_code = models.CharField(max_length=20)
    section = models.CharField(max_length=10)
    credit_hours = models.IntegerField()
    name = models.CharField(max_length=75)
    upload_set = models.ForeignKey(UploadSet, on_delete=models.CASCADE)

    class Meta:
        _index_fields = ["course_code", "section", "upload_set"]
        indexes = [
            models.Index(fields=_index_fields, name="course_index"),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=_index_fields,
                name="unique_course_index_constraint",
            )
        ]


class Enrolment(models.Model):
    id = models.BigAutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    term = models.CharField(max_length=10)
    grade = models.CharField(max_length=5)
    upload_set = models.ForeignKey(UploadSet, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=["term"], name="enrolment_index"),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["student_id", "course_id"], name="unique_enrolment_constraint"
            )
        ]

    def __str__(self):
        return f"Enrolment: {self.id} (Student: {self.student.student_number}) (Course Section: {self.course.section})"


class PreReq(models.Model):
    id = models.BigAutoField(primary_key=True)
    course_code = models.CharField(max_length=10)
    rank = models.CharField(max_length=3)

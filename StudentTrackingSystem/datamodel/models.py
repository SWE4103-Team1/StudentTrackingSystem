from django.db import models


class UploadSet(models.Model):
    upload_date = models.DateField(primary_key=True)
    # must be sure that
    person_data_file = models.FileField(upload_to="uploads/")
    course_data_file = models.FileField(upload_to="uploads/")
    transfer_data_file = models.FileField(upload_to="uploads/")


class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    student_number = models.IntegerField()
    name = models.TextField(max_length=70)
    gender = models.CharField(max_length=1)
    address = models.TextField(max_length=140)
    email = models.EmailField(max_length=50)
    campus = models.CharField(max_length=2)
    program = models.CharField(max_length=10)
    start_date = models.DateField(max_length=8)
    upload_date = models.ForeignKey(UploadSet, on_delete=models.CASCADE)

    class Meta:
        _index_fields = ["student_number", "upload_date"]
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
        return f"sid: {self.sid}, name: {self.name}, gender: {self.gender}, address: {self.address}, email: {self.email}"


class Course(models.Model):
    id = models.BigAutoField(primary_key=True)
    course_code = models.CharField(max_length=20)
    section = models.CharField(max_length=10)
    credit_hours = models.IntegerField()
    name = models.CharField(max_length=50)
    upload_date = models.ForeignKey(UploadSet, on_delete=models.CASCADE)

    class Meta:
        _index_fields = ["course_code", "section", "upload_date"]
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
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    term = models.CharField(max_length=10)
    grade = models.CharField(max_length=5)
    upload_date = models.ForeignKey(UploadSet, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["student_id", "course_id"], name="unique_enrolment_constraint"
            )
        ]

    def __str__(self):
        return f"Enrolment: {self.id} (Student: {self.sid}) (Course Section: {self.section})"

from django.db import models
from django.db.models.fields import CharField

class Student(models.Model):
        sid = models.IntegerField(max_length=8, primary_key=True)
        name = models.CharField(max_length=70)
        gender = models.CharField(max_length=1)
        address = models.TextField(max_length=140)
        email = models.EmailField(max_length=50)
        campus = models.CharField(max_length=2)
        program = models.CharField(max_length=10)
        start_date = models.DateField(max_length=8)

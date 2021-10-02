from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email address", unique=True, max_length=255)
    username = models.CharField(max_length=255)
    role = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = (
        "email"  # makes email the primary key for default authentication backend
    )
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["role"]

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

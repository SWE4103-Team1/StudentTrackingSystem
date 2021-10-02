from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


class User(AbstractUser):
    # username & password from AbstractUser
    email = models.EmailField(verbose_name="email address", unique=True, max_length=255)
    role = models.IntegerField()

    USERNAME_FIELD = (
        "email"  # makes email the primary key for default authentication backend
    )

    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["role"]  # in addition to USERNAME_FIELD and password

    objects = UserManager()

    def __str__(self):
        return self.email

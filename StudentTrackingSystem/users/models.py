from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


class User(AbstractUser):
    # username & password from AbstractUser
    email = models.EmailField(verbose_name="email address", unique=True, max_length=255)
    role = models.IntegerField()
    username = models.CharField(
        "username",
        max_length=150,
        unique=True,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[UnicodeUsernameValidator()],
        error_messages={
            "unique": "A user with that username already exists.",
        },
        blank=True,
    )

    USERNAME_FIELD = (
        "email"  # makes email the primary key for default authentication backend
    )

    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["role"]  # in addition to USERNAME_FIELD and password

    objects = UserManager()

    def __str__(self):
        return self.email

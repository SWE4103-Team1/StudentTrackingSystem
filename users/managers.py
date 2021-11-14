from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from .roles import UserRole


class UserManager(BaseUserManager):
    """
    User model using email as the unique identifier.
    Also contains role to differentiate user types
    """

    def create_user(
        self, email: str, password: str, username: str, role: UserRole, **extra_fields
    ):
        err_msg = "{} must be provided to create a user"
        if not email:
            raise ValueError(err_msg.format("Email"))
        if not password:
            raise ValueError(err_msg.format("Password"))
        if not role:
            raise ValueError(err_msg.format("Role"))

        email = self.normalize_email(email)
        username = (
            username if username else ""
        )  # django user model can't have username = Null

        user = self.model(email=email, username=username, role=role, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self, email: str, password: str, username: str, role: UserRole, **extra_fields
    ):
        err_msg = "{} must be provided to create a user"
        if not email:
            raise ValueError(err_msg.format("Email"))
        if not password:
            raise ValueError(err_msg.format("Password"))
        if not role:
            raise ValueError(err_msg.format("Role"))

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, username, role, **extra_fields)

    def login_user(self, username: str, password: str):
        if not username:
            raise ValueError(err_msg.format("username"))
        if not password:
            raise ValueError(err_msg.format("Password"))

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(user)
            return True
        else:
            return False

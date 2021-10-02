from django.contrib.auth.base_user import BaseUserManager

from .user_roles import UserRole


class UserManager(BaseUserManager):
    """
    User model using email as the unique identifier.
    Also contains role to differentiate user types
    """

    def create_user(self, email: str, password: str, username: str, role: UserRole):
        err_msg = "{} must be provided to create a user"
        if not email:
            raise ValueError(err_msg.format("Email"))
        if not password:
            raise ValueError(err_msg.format("Password"))
        if not role:
            raise ValueError(err_msg.format("Role"))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, role=role)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self, email: str, password: str, username: str, role: UserRole
    ):
        err_msg = "{} must be provided to create a user"
        if not email:
            raise ValueError(err_msg.format("Email"))
        if not password:
            raise ValueError(err_msg.format("Password"))
        if not role:
            raise ValueError(err_msg.format("Role"))

        user = self.create_user(
            email=email, password=password, username=username, role=role
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

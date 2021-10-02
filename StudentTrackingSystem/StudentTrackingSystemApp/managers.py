from django.contrib.auth.base_user import BaseUserManager

class UserManager():
    """
    User model using email as the unique identifier.
    Also contains role to differentiate user types
    """

    def create_user(self, email, ):

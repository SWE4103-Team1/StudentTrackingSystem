from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User

admin.site.register(User, UserAdmin)

# TODO: may need to create a custom UserAdmin such that it displays all fields from the custom User model

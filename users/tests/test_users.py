from django.test import TestCase
from django.contrib.auth import get_user_model

from ..roles import UserRole

class UserManagerTests(TestCase):
    def test_create_basic_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email="normal@user.com",
            password="foo",
            username=None,
            role=UserRole.AccredidationCoordinator,
        )
        self.assertEqual(user.email, "normal@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        try:
            self.assertIsNotNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="", password="foo")

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email="normal@user.com",
            password="foo",
            username="normal",
            role=UserRole.AccredidationCoordinator,
        )
        self.assertEqual(user.email, "normal@user.com")
        self.assertEqual(user.username, "normal")
        self.assertEqual(user.role, UserRole.AccredidationCoordinator)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email="super@user.com",
            password="foo",
            username="super",
            role=UserRole.ProgramAdvisor,
        )
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertEqual(admin_user.username, "super")
        self.assertEqual(admin_user.role, UserRole.ProgramAdvisor)
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        try:
            self.assertIsNotNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_superuser(email="super@user.com", password="foo")
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="super@user.com",
                password="foo",
                username=None,
                role=UserRole.ProgramAdvisor,
                is_superuser=False,
            )

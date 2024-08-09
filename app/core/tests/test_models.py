"""testing models"""
from django.test import TestCase
from core.models import User


class UserModelTest(TestCase):
    """Testing the user model"""

    def setUp(self):
        """Set up the data for user model"""
        self.valid_email = "test@example.com"
        self.invalid_email = "invalid-email"
        self.password = "StrongPassword123"
        self.weak_password = "123"

    def test_create_user_with_valid_email(self):
        """Testing creating user with valid email"""
        user = User.objects.create_user(email=self.valid_email,
                                        password=self.password)
        self.assertEqual(user.email, self.valid_email)
        self.assertTrue(user.check_password(self.password))

    def test_create_user_with_invalid_email(self):
        """Testing creating user with invalid email"""
        with self.assertRaises(ValueError):
            User.objects.create_user(email=self.invalid_email,
                                     password=self.password)

    def test_create_user_with_invalid_password(self):
        """Testing creating user with invalid password."""
        with self.assertRaises(ValueError):
            User.objects.create_user(email=self.invalid_email,
                                     password=self.weak_password)

    def test_create_superuser(self):
        """Testing creating superusers"""
        admin_user = User.objects.create_superuser(email=self.valid_email,
                                                   password=self.password)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_admin)

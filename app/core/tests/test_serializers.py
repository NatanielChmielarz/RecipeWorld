"""Testing serialization"""
from django.test import TestCase
from core.models import User
from user_app.serializers import SignupSerializer


class SignupSerializerTest(TestCase):
    """Class for testing the SignupSerializer"""

    def setUp(self):
        """set up valid and invalid data"""
        self.valid_data = {
            'email': 'test@example.com',
            'password': 'StrongPassword123',
            'confirm_password': 'StrongPassword123'
        }
        self.invalid_data = {
            'email': 'test@example.com',
            'password': 'StrongPassword123',
            'confirm_password': 'WrongPassword123'
        }

    def test_valid_data(self):
        """testing valid data"""
        serializer = SignupSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_password_confirmation(self):
        """test that the password confirmation"""
        serializer = SignupSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('password_mismatch', serializer.errors)

    def test_email_already_exists(self):
        """test that the email already exists"""
        User.objects.create_user(email=self.valid_data['email'],
                                 password=self.valid_data['password'])
        serializer = SignupSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)
        self.assertEqual(serializer.errors['email'][0],
                         'user with this email already exists.')

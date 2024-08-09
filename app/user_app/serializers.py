from rest_framework import serializers
from core.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password


class SignupSerializer(serializers.ModelSerializer):
    """The sign up serializer class"""

    confirm_password = serializers.CharField(
        style={'input_style': 'password'},
        write_only=True)

    class Meta:
        """Meta class for signup serializers including fields :
        email, password, confirm_password."""

        model = User
        fields = ('email', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        """Validation method checking that passwords are the same"""

        # Check if passwords match
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError(
                {'password_mismatch': 'Password fields did not match.'})

        # Check if email already exists
        if User.objects.filter(email=data.get("email")).exists():
            raise serializers.ValidationError(
                {'email': 'User with this email already exists.'})

        return data

    def create(self, validated_data):
        """Method to create a new user"""
        # Remove confirm_password from validated_data
        validated_data.pop('confirm_password')

        # Create the user
        if validate_password(validated_data['password']) is None:
            validated_data['password'] = make_password(
                                        validated_data['password'])
            return User.objects.create(**validated_data)

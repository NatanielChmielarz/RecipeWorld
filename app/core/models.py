"""
Creating models for a project
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


class UserManager(BaseUserManager):
    """Creating a new user manager"""

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not re.fullmatch(regex, email):
            raise ValueError('Invalid email address')

        user = self.model(email=self.normalize_email(email),)
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password=None):
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email,  password=None):
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    """User class"""

    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

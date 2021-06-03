import datetime

from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
)

# Create your models here.
from .utils import get_semester

DEFAULT_FIELDS_MAX_LENGTH = settings.DEFAULT_FIELDS_MAX_LENGTH


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        if not email.endswith('kpfu.ru'):
            raise ValueError('The Email should be in kpfu.ru domain')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
        Student model, able to vote.
    """
    username = None
    email = models.EmailField(
        max_length=DEFAULT_FIELDS_MAX_LENGTH, unique=True, blank=False)
    admission_year = models.PositiveSmallIntegerField(blank=True, null=True, unique=False, default=2018)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def name(self):
        return f'{self.email[:self.email.index("@")]}'

    def __str__(self):
        return f'{self.admission_year} {self.email}'

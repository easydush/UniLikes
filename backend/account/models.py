from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
)

# Create your models here.
DEFAULT_FIELDS_MAX_LENGTH = settings.DEFAULT_FIELDS_MAX_LENGTH


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        if not email.endswith('kpfu.ru'):
            raise ValueError('The Email should be in kpfu domain')
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
    username = None
    email = models.EmailField(
        max_length=DEFAULT_FIELDS_MAX_LENGTH, unique=True, blank=False)
    admission_year = models.PositiveSmallIntegerField(blank=True, null=True, unique=False)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.admission_year} {self.email[:self.email.index("@")]}'


class Teacher(models.Model):
    username = None
    name = models.CharField(max_length=DEFAULT_FIELDS_MAX_LENGTH)
    patronymic = models.CharField(max_length=DEFAULT_FIELDS_MAX_LENGTH)
    surname = models.CharField(max_length=DEFAULT_FIELDS_MAX_LENGTH)
    photo_url = models.URLField(null=True,
                                default='https://secure.gravatar.com/avatar/0fb68a3652b2d19b550a3fca1e71d9cc?s=4729128&d=mm')
    rating = models.FloatField(null=True)

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'


class TeacherSubjectCourse(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.CharField(max_length=DEFAULT_FIELDS_MAX_LENGTH)
    semester = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.teacher.surname} | {self.subject}, {self.semester} семестр'

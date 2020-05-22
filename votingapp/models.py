from django.contrib.auth.base_user import BaseUserManager
from django.db.models import Avg
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser

COURSE_CHOICES = [
    (1, '1 - бакалавриат'),
    (2, '2 - бакалавриат'),
    (3, '3 - бакалавриат'),
    (4, '4 - бакалавриат'),
    (5, '1 - магистратура'),
    (6, '2 - магистратура'),
]


# class StudentManager(BaseUserManager):
#     use_in_migrations = True
#
#     def _create_user(self, email, password, **extra_fields):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('The given email must be set')
#
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)
#
#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_superuser', True)
#
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self._create_user(email, password, **extra_fields)


class Student(AbstractUser):
    course = models.IntegerField(
        choices=COURSE_CHOICES,
        default=1)
    semesters = models.SlugField

    def __str__(self):
        return f'{self.email[:self.email.index("@")]}, {self.course}'

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'


class Subject(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    surname = models.CharField(max_length=30, verbose_name='Surname')
    name = models.CharField(max_length=30, verbose_name='Name')
    second_name = models.CharField(max_length=30, verbose_name='Second name')
    photo = models.ImageField(verbose_name='Photo', upload_to='votingapp/teacher/photos', default='defaulteacher.jpg',
                              blank=True)

    def __str__(self):
        return self.surname + ' ' + self.name + ' ' + self.second_name

    def __rating__(self):
        return Rate.objects.filter(teacher=self).aggregate(Avg('rate'))


class TeacherSubjectCourse(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    semester = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.subject.title}, {self.semester} курс'


class Rate(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(Teacher, verbose_name='Teacher', on_delete=models.CASCADE)
    RATE_CHOICES = [
        (1, '1'),
        (-1, '-1'),
        (0, '0')]
    rate = models.PositiveSmallIntegerField(verbose_name='Rate', choices=RATE_CHOICES,
                                            default=0)

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


class Student(AbstractUser):
    course = models.IntegerField(
        choices=COURSE_CHOICES,
        default=1)
    semesters = models.SlugField(default='0', null=True, blank=True)

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
    photo_url = models.URLField(null=True,
                                default='https://secure.gravatar.com/avatar/0fb68a3652b2d19b550a3fca1e71d9cc?s=4729128&d=mm')

    def full_name(self):
        return "%s %s %s" % (self.surname, self.name, self.second_name)

    def __str__(self):
        return self.surname + ' ' + self.name + ' ' + self.second_name


class TeacherSubjectCourse(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    semester = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.teacher.surname} | {self.subject.title}, {self.semester} семестр'


class Rate(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(Teacher, verbose_name='Teacher', on_delete=models.CASCADE)
    RATE_CHOICES = [
        (1, '1'),
        (-1, '-1'),
        (0, '0')]
    # -1 means that it's not your teacher
    rate = models.SmallIntegerField(verbose_name='Rate', choices=RATE_CHOICES,
                                    default=0)

    def __str__(self):
        return f'{self.timestamp}|{self.rate} for {self.teacher.surname}'


class StudTeachRateFact(models.Model):
    """Sounds bad, but this model is a guarantee for anonymous voting and defends user from
    repeating vote. It's not linked to Rate, because of anonymous."""
    timestamp = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(Teacher, verbose_name='Teacher', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, verbose_name='Student', on_delete=models.CASCADE)
    semester = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.student.username} voted for {self.teacher.surname} in {self.semester} semester'

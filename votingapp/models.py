from django.db.models import Avg
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser


class Student(AbstractUser):
    course = models.IntegerField(null=True,
                                 # validators=[MinValueValidator(1), MaxValueValidator(6)],
                                 verbose_name='Курс')

    def __str__(self):
        return self.course


class Subject(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    surname = models.CharField(max_length=30, verbose_name='Surname')
    name = models.CharField(max_length=30, verbose_name='Name')
    second_name = models.CharField(max_length=30, verbose_name='Second name')
    photo = models.ImageField(verbose_name='Photo', upload_to='votingapp/photos', default='', blank=True)

    def __str__(self):
        return self.surname + ' ' + self.name + ' ' + self.second_name

    def __rating__(self):
        return Rate.objects.filter(teacher=self).aggregate(Avg('rate'))


class CourseSubject(models.Model):
    teacher = models.ManyToManyField(Teacher)
    course = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.course + '' + self.subject


class Rate(models.Model):
    teacher = models.ForeignKey(Teacher, verbose_name='Teacher', on_delete=models.CASCADE)
    rate = models.IntegerField(verbose_name='Rate')

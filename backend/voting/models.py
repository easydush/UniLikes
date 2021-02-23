from django.db import models
from account.models import User

from django.conf import settings

DEFAULT_FIELDS_MAX_LENGTH = settings.DEFAULT_FIELDS_MAX_LENGTH


class Teacher(models.Model):
    username = None
    name = models.CharField(max_length=DEFAULT_FIELDS_MAX_LENGTH)
    patronymic = models.CharField(max_length=DEFAULT_FIELDS_MAX_LENGTH)
    surname = models.CharField(max_length=DEFAULT_FIELDS_MAX_LENGTH)
    photo_url = models.URLField(null=True,
                                default='https://secure.gravatar.com/avatar/0fb68a3652b2d19b550a3fca1e71d9cc?s=4729128&d=mm')
    rating = models.FloatField(null=True)
    vote_counts = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'


class TeacherSubjectSemester(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.CharField(max_length=DEFAULT_FIELDS_MAX_LENGTH)
    semester = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.teacher.surname} | {self.subject}, {self.semester} семестр'


class RateFact(models.Model):
    """Sounds bad, but this model is a guarantee for anonymous voting and defends user from
    repeating vote. It's not linked to Rate, because of anonymous."""
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.student} voted for {self.teacher} in {self.semester} semester'

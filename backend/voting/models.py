from django.db import models
from account.models import User
from teacher.models import Teacher
from django.conf import settings

DEFAULT_FIELDS_MAX_LENGTH = settings.DEFAULT_FIELDS_MAX_LENGTH


class TeacherSubjectSemester(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='subjects_semesters')
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

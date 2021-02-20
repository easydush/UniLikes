from django.db import models

# Create your models here.
from backend.account.models import Teacher, User


class RateFact(models.Model):
    """Sounds bad, but this model is a guarantee for anonymous voting and defends user from
    repeating vote. It's not linked to Rate, because of anonymous."""
    timestamp = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(Teacher, verbose_name='Teacher', on_delete=models.CASCADE)
    student = models.ForeignKey(User, verbose_name='Student', on_delete=models.CASCADE)
    semester = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.student} voted for {self.teacher} in {self.semester} semester'

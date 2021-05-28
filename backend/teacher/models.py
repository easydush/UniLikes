from django.db import models

# Create your models here.
from UniLikes.settings import DEFAULT_FIELDS_MAX_LENGTH


class Teacher(models.Model):
    username = None
    name = models.CharField(max_length=DEFAULT_FIELDS_MAX_LENGTH)
    patronymic = models.CharField(max_length=DEFAULT_FIELDS_MAX_LENGTH)
    surname = models.CharField(max_length=DEFAULT_FIELDS_MAX_LENGTH)
    photo_url = models.URLField(null=True,
                                default='https://secure.gravatar.com/avatar/0fb68a3652b2d19b550a3fca1e71d9cc?s=4729128&d=mm')
    rating = models.FloatField(default=0)
    vote_counts = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'

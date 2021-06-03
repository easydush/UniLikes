from django.db import models

from UniLikes.settings import DEFAULT_FIELDS_MAX_LENGTH, DEFAULT_AVATAR


class Teacher(models.Model):
    """
        Teacher for voting. Can be added by admin only.
    """
    username = None
    name = models.CharField(max_length=DEFAULT_FIELDS_MAX_LENGTH)
    patronymic = models.CharField(max_length=DEFAULT_FIELDS_MAX_LENGTH)
    surname = models.CharField(max_length=DEFAULT_FIELDS_MAX_LENGTH)
    photo_url = models.URLField(null=True,
                                default=DEFAULT_AVATAR)
    rating = models.FloatField(default=0)
    vote_counts = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'

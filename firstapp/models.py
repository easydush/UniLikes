from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=30, verbose_name='Teacher')
    rating = models.FloatField(default=0, verbose_name='Rating')
    url = models.URLField(verbose_name='KFU account')
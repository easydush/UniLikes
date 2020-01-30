from django.db import models


class Teacher(models.Model):
    surname = models.CharField(max_length=30, verbose_name='Surname')
    name = models.CharField(max_length=30, verbose_name='Name')
    second_name = models.CharField(max_length=30, verbose_name='Second name')
    rating = models.FloatField(default=0, verbose_name='Rating')
    photo_url = models.URLField(verbose_name='Photo')

    def __str__(self):
        return self.surname + ' ' + self.name + ' ' + self.second_name


class Subject(models.Model):
    title = models.CharField(max_length=30)


class CourseSubjectTeacher(models.Model):
    course = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

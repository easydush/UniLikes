# Generated by Django 3.1.6 on 2021-02-23 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0002_auto_20210223_1409'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachersubjectcourse',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='patronymic',
        ),
        migrations.RemoveField(
            model_name='user',
            name='surname',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.DeleteModel(
            name='TeacherSubjectCourse',
        ),
    ]

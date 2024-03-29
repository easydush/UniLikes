# Generated by Django 3.1.6 on 2021-02-23 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('patronymic', models.CharField(max_length=60)),
                ('surname', models.CharField(max_length=60)),
                ('photo_url', models.URLField(default='https://secure.gravatar.com/avatar/0fb68a3652b2d19b550a3fca1e71d9cc?s=4729128&d=mm', null=True)),
                ('rating', models.FloatField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='ratefact',
            name='timestamp',
        ),
        migrations.AlterField(
            model_name='ratefact',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='TeacherSubjectSemester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=60)),
                ('semester', models.PositiveSmallIntegerField(default=0)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.teacher')),
            ],
        ),
        migrations.AlterField(
            model_name='ratefact',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.teacher'),
        ),
    ]

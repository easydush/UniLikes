# Generated by Django 3.2 on 2021-05-20 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
        ('voting', '0003_auto_20210505_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratefact',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher'),
        ),
        migrations.AlterField(
            model_name='teachersubjectsemester',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher'),
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]

# Generated by Django 3.2 on 2021-05-20 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='vote_counts',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
    ]
# Generated by Django 3.2 on 2021-05-21 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_user_admission_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='admission_year',
            field=models.PositiveSmallIntegerField(blank=True, default=9998, null=True),
        ),
    ]

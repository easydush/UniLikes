# Generated by Django 3.2 on 2021-05-21 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_user_admission_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='admission_year',
            field=models.PositiveSmallIntegerField(blank=True, default=2018, null=True),
        ),
    ]
# Generated by Django 3.2 on 2021-05-20 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('patronymic', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('photo_url', models.URLField(default='https://secure.gravatar.com/avatar/0fb68a3652b2d19b550a3fca1e71d9cc?s=4729128&d=mm', null=True)),
                ('rating', models.FloatField(null=True)),
                ('vote_counts', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
    ]

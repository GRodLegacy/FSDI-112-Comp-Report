# Generated by Django 2.1 on 2019-10-25 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_director'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name_plural': 'Movies'},
        ),
    ]

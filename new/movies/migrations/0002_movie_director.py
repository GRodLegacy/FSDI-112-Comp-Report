# Generated by Django 2.1 on 2019-10-24 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default='director', max_length=255),
            preserve_default=False,
        ),
    ]
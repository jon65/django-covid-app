# Generated by Django 3.2.7 on 2021-10-09 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210909_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='counter',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

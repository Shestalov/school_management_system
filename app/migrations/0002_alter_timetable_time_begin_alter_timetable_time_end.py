# Generated by Django 4.1.3 on 2022-11-19 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='time_begin',
            field=models.TimeField(verbose_name='%H:%M'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='time_end',
            field=models.TimeField(verbose_name='%H:%M'),
        ),
    ]
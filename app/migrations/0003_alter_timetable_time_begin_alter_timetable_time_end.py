# Generated by Django 4.1.3 on 2022-11-19 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_timetable_time_begin_alter_timetable_time_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='time_begin',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='time_end',
            field=models.TimeField(),
        ),
    ]

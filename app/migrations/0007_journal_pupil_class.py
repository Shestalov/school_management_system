# Generated by Django 4.1.3 on 2022-11-22 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_timetable_time_begin_alter_timetable_time_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='pupil_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.classes'),
        ),
    ]

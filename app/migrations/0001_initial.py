# Generated by Django 4.1.3 on 2022-11-19 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name_teacher', models.CharField(max_length=50)),
                ('second_name_teacher', models.CharField(max_length=50)),
                ('teachers_clas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.classes')),
                ('teaching_lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.lessons')),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20)),
                ('time_begin', models.TimeField()),
                ('time_end', models.TimeField()),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.classes')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.lessons')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.teachers')),
            ],
        ),
        migrations.CreateModel(
            name='Pupils',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name_pupil', models.CharField(max_length=50)),
                ('second_name_pupil', models.CharField(max_length=50)),
                ('current_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.classes')),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('mark', models.IntegerField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.lessons')),
                ('pupils', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pupils')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.teachers')),
            ],
        ),
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.lessons')),
                ('pupil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pupils')),
            ],
        ),
    ]

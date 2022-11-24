from django.db import models


class Classes(models.Model):
    class_name = models.CharField(max_length=10)


class Lessons(models.Model):
    lesson_name = models.CharField(max_length=50)


class Pupils(models.Model):
    first_name_pupil = models.CharField(max_length=50)
    second_name_pupil = models.CharField(max_length=50)
    current_class = models.ForeignKey(Classes, on_delete=models.CASCADE, null=True)


class Teachers(models.Model):
    first_name_teacher = models.CharField(max_length=50)
    second_name_teacher = models.CharField(max_length=50)
    teachers_lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    teachers_class = models.ForeignKey(Classes, on_delete=models.CASCADE)


class TimeTable(models.Model):
    class_name = models.ForeignKey(Classes, on_delete=models.CASCADE)
    day = models.CharField(max_length=20)
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    time_begin = models.CharField(max_length=5)
    time_end = models.CharField(max_length=5)


class Journal(models.Model):
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    pupil = models.ForeignKey(Pupils, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    pupils_class = models.ForeignKey(Classes, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    mark = models.IntegerField()


class Absence(models.Model):
    pupil = models.ForeignKey(Pupils, on_delete=models.CASCADE)
    date = models.DateField()
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)

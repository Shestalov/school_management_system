from django.shortcuts import render, redirect
from django.contrib import messages
from . import models
import datetime


def login(request):
    return render(request, 'app/login.html')


def logout(request):
    return render(request, 'app/logout.html')


def home(request):
    classes = models.Classes.objects.all()
    classes_related = classes.prefetch_related('pupils_set').all()
    lessons = models.Lessons.objects.all()
    pupils = models.Pupils.objects.all().prefetch_related('current_class').all()
    uniq_teachers = models.Teachers.objects.values('second_name_teacher', 'first_name_teacher').distinct()

    data = {'classes': classes, 'lessons': lessons, 'teachers': uniq_teachers,
            'pupils': pupils, 'classes_related': classes_related}
    return render(request, 'app/home.html', data)


# without prefect related
def filter_pupils(request):
    classes = models.Classes.objects.all()

    if request.method == 'GET':
        return render(request, 'app/filter_pupils.html', {'classes': classes})
    else:
        class_name = request.POST.get('class_name')

        if class_name == 'All pupils':
            pupils_in = models.Pupils.objects.all()
        else:
            current_class = models.Classes.objects.filter(class_name=class_name).first()
            pupils_in = models.Pupils.objects.filter(current_class=current_class.id).all()

        data = {'classes': classes, 'pupils': pupils_in, 'class_name': class_name}
        return render(request, 'app/filter_pupils.html', data)


def add_pupil(request):
    if request.method == 'GET':
        classes = models.Classes.objects.all()
        return render(request, 'app/add_pupil.html', {'classes': classes})
    else:
        first_name_pupil = request.POST.get('first_name_pupil')
        second_name_pupil = request.POST.get('second_name_pupil')
        get_pupil_class = request.POST.get('pupil_class')

        pupil_class = models.Classes.objects.filter(class_name=get_pupil_class).first()

        is_pupil = models.Pupils.objects.filter(first_name_pupil=first_name_pupil,
                                                second_name_pupil=second_name_pupil,
                                                current_class=pupil_class).exists()
        if is_pupil:
            messages.error(request, f'The pupil "{second_name_pupil} {first_name_pupil}" '
                                    f'in "{get_pupil_class}" is already exists')
            return redirect('app:add_pupil')
        else:
            new_pupil = models.Pupils.objects.create(first_name_pupil=first_name_pupil,
                                                     second_name_pupil=second_name_pupil,
                                                     current_class=pupil_class)
            new_pupil.save()
            messages.success(request,
                             f'Pupil "{second_name_pupil} {first_name_pupil}" in "{get_pupil_class}" was added')
            return redirect('app:add_pupil')


def delete_pupil(request):
    if request.method == 'GET':
        pupils = models.Pupils.objects.all()
        return render(request, 'app/delete_pupil.html', {'pupils': pupils})
    else:
        pupil_id = request.POST.get('delete_pupil')
        models.Pupils.objects.filter(pk=pupil_id).delete()
        messages.success(request, 'Pupil was deleted')
        return redirect('app:delete_pupil')


# with prefetch related
def filter_teachers(request):
    classes = models.Classes.objects.all()

    if request.method == 'GET':
        return render(request, 'app/filter_teachers.html', {'classes': classes})
    else:
        class_id = request.POST.get('class_id')

        teachers = models.Teachers.objects.filter(teachers_class=class_id) \
            .prefetch_related('teachers_lesson').prefetch_related('teachers_class').all()

        data = {'classes': classes, 'teachers': teachers}
        return render(request, 'app/filter_teachers.html', data)


def add_teacher(request):
    if request.method == 'GET':
        classes = models.Classes.objects.all()
        lessons = models.Lessons.objects.all()

        data = {'classes': classes, 'lessons': lessons}
        return render(request, 'app/add_teacher.html', data)
    else:
        first_new_name_teacher = request.POST.get('first_new_name_teacher')
        second_new_name_teacher = request.POST.get('second_new_name_teacher')
        teachers_class = request.POST.get('teacher_class')
        teachers_lesson = request.POST.get('teacher_lesson')

        teacher_class = models.Classes.objects.filter(class_name=teachers_class).first()
        teacher_lesson = models.Lessons.objects.filter(lesson_name=teachers_lesson).first()

        checking_teacher = models.Teachers.objects.filter(first_name_teacher=first_new_name_teacher,
                                                          second_name_teacher=second_new_name_teacher,
                                                          teachers_class=teacher_class,
                                                          teachers_lesson=teacher_lesson).exists()
        if checking_teacher:
            messages.error(request, f'The teacher "{second_new_name_teacher} {first_new_name_teacher}" '
                                    f'in "{teachers_class} {teachers_lesson} "is already exists')
            return redirect('app:add_teacher')
        else:
            new_teacher = models.Teachers.objects.create(first_name_teacher=first_new_name_teacher,
                                                         second_name_teacher=second_new_name_teacher,
                                                         teachers_class=teacher_class,
                                                         teachers_lesson=teacher_lesson)
            new_teacher.save()
            messages.success(request, f'New teacher "{second_new_name_teacher} {first_new_name_teacher}" '
                                      f'was added in "{teachers_class} {teachers_lesson}"')
            return redirect('app:add_teacher')


def delete_teacher(request):
    if request.method == 'GET':
        teachers = models.Teachers.objects.all().prefetch_related('teachers_class').all()
        return render(request, 'app/delete_teacher.html', {'teachers': teachers})
    else:
        teacher = request.POST.get('teacher_id')
        models.Teachers.objects.filter(pk=teacher).delete()
        messages.success(request, 'Teacher was deleted')
        return redirect('app:delete_teacher')


def add_class(request):
    classes = models.Classes.objects.all()

    if request.method == 'GET':
        return render(request, 'app/add_class.html', {'classes': classes})
    else:
        new_class_name = request.POST.get('new_class_name')
        classes_list = [itm.class_name for itm in classes]

        if new_class_name in classes_list:
            messages.error(request, f'Class {new_class_name} is already exist')
            return redirect('app:add_class')
        else:
            new_class = models.Classes.objects.create(class_name=new_class_name)
            new_class.save()
            messages.success(request, f'Class {new_class_name} was added')
            return redirect('app:add_class')


def delete_class(request):
    if request.method == 'GET':
        classes = models.Classes.objects.all()
        return render(request, 'app/delete_class.html', {'classes': classes})
    else:
        delete_class_name = request.POST.get('delete_class_name')
        models.Classes.objects.filter(class_name=delete_class_name).delete()
        messages.success(request, f'Class {delete_class_name} was deleted')
        return redirect('app:delete_class')


def classes_journals(request):
    classes = models.Classes.objects.all()
    lessons = models.Lessons.objects.all()

    if request.method == 'GET':
        data = {'classes': classes, 'lessons': lessons}
        return render(request, 'app/classes_journals.html', data)
    else:
        pupils_class = request.POST.get('pupils_class')
        pupils_lesson = request.POST.get('pupils_lesson')

        class_id = models.Classes.objects.filter(class_name=pupils_class).first()
        current_lesson_id = models.Lessons.objects.filter(lesson_name=pupils_lesson).first()
        journal_res = models.Journal.objects.filter(lesson=current_lesson_id, pupils_class=class_id).all()
        journal_related = journal_res.prefetch_related('pupil').all()

        all_pupils_in_current_class = set(
            f"{itm.pupil.second_name_pupil} {itm.pupil.first_name_pupil}" for itm in journal_related)

        data = {'class': class_id,
                'classes': classes,
                'lessons': lessons,
                'lesson': current_lesson_id,
                'journal': journal_res,
                'pupils': journal_related,
                'all_pupils_in_current_class': all_pupils_in_current_class}

        return render(request, 'app/classes_journals.html', data)


def add_mark(request):
    if request.method == 'GET':
        marks = [i for i in range(1, 13)]
        teachers = models.Teachers.objects.all().prefetch_related('teachers_class').prefetch_related(
            'teachers_lesson').order_by('first_name_teacher')
        pupils = models.Pupils.objects.all().prefetch_related('current_class').all()
        data = {'marks': marks, 'teachers': teachers, 'pupils': pupils}
        return render(request, 'app/add_mark.html', data)
    else:
        user_mark = request.POST.get('mark')
        user_pupil = request.POST.get('pupil')
        user_teacher = request.POST.get('teacher')
        date = datetime.date.today()

        teacher = models.Teachers.objects.filter(pk=user_teacher).first()
        pupil = models.Pupils.objects.filter(pk=user_pupil).first()

        models.Journal.objects.create(date=date, mark=user_mark,
                                      lesson=teacher.teachers_lesson, teacher=teacher,
                                      pupil=pupil, pupils_class=pupil.current_class)

        messages.success(request, 'Mark was added')
        return redirect('app:add_mark')


def timetable(request):
    classes = models.Classes.objects.all()

    if request.method == 'GET':
        return render(request, 'app/timetable.html', {'classes': classes})
    else:
        day = request.POST.get('day')
        class_name = request.POST.get('class_name')

        selected_class = models.Classes.objects.filter(class_name=class_name).first()

        if day == 'All weak':
            time_table = models.TimeTable.objects.filter(class_name_id=selected_class.id).all()
        else:
            time_table = models.TimeTable.objects.filter(class_name_id=selected_class.id, day=day).all()

        related = time_table.prefetch_related('lesson').all().prefetch_related('class_name').all().prefetch_related(
            'teacher').all()
        days = list(set(itm.day for itm in related))
        result = {'result': related, 'classes': classes, 'day': day, 'class_name': class_name, 'days': days}

        return render(request, 'app/timetable.html', result)


def add_timetable(request):
    time = ['09:00 - 09:35', '09:50 - 10:25', '10:55 - 11:30', '12:05 - 12:40', '12:55 - 13:30']

    if request.method == 'GET':
        lessons = models.Lessons.objects.all()
        teachers = models.Teachers.objects.all().prefetch_related('teachers_class').all().order_by('first_name_teacher')
        classes = models.Classes.objects.all()
        data = {'lessons': lessons, 'teachers': teachers, 'classes': classes, 'time': time}
        return render(request, 'app/add_timetable.html', data)
    else:
        user_teacher_id = request.POST.get('teacher_id')
        user_time = request.POST.get('time')
        user_class_id = request.POST.get('class_id')
        user_day = request.POST.get('day')
        user_time_begin = time[int(user_time)][:5]
        user_time_end = time[int(user_time)][8:]

        teacher = models.Teachers.objects.filter(pk=user_teacher_id).prefetch_related('teachers_lesson').first()
        lesson = models.Lessons.objects.get(pk=teacher.teachers_lesson.id)
        class_id = models.Classes.objects.get(pk=user_class_id)

        existing_timetable = models.TimeTable.objects.filter(day=user_day,
                                                             time_begin=user_time_begin,
                                                             time_end=user_time_end,
                                                             class_name=class_id,
                                                             lesson=teacher.teachers_lesson.id,
                                                             teacher=teacher.id).exists()
        if existing_timetable:
            messages.error(request, 'Timetable already exist')
            return redirect('app:add_timetable')
        else:
            models.TimeTable.objects.create(day=user_day,
                                            time_begin=user_time_begin,
                                            time_end=user_time_end,
                                            class_name=class_id,
                                            lesson=lesson,
                                            teacher=teacher)
            messages.success(request, f'Timetable {teacher.second_name_teacher} {teacher.first_name_teacher}, '
                                      f'{teacher.teachers_lesson.lesson_name}, {teacher.teachers_class.class_name},'
                                      f' {user_day}, {user_time_begin}, {user_time_end} was added')
            return redirect('app:add_timetable')


def delete_timetable(request, timetable_id):
    models.TimeTable.objects.get(pk=timetable_id).delete()
    messages.success(request, 'Timetable was deleted')
    return redirect('app:timetable')

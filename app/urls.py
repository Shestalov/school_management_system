from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),

    path('timetable', views.timetable, name='timetable'),
    path('add_timetable', views.add_timetable, name='add_timetable'),
    path('timetable/<int:timetable_id>/delete_timetable', views.delete_timetable, name='delete_timetable'),

    path('classes_journals', views.classes_journals, name='classes_journals'),
    path('add_mark', views.add_mark, name='add_mark'),

    path('add_class', views.add_class, name='add_class'),
    path('delete_class', views.delete_class, name='delete_class'),

    path('filter_pupils', views.filter_pupils, name='filter_pupils'),

    path('add_pupil', views.add_pupil, name='add_pupil'),
    path('delete_pupil', views.delete_pupil, name='delete_pupil'),

    path('filter_teachers', views.filter_teachers, name='filter_teachers'),
    path('add_teacher', views.add_teacher, name='add_teacher'),
    path('delete_teacher', views.delete_teacher, name='delete_teacher'),

    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]

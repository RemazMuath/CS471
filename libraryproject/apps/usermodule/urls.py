from django.urls import path
from . import views

urlpatterns = [
    path('lab8/task7', views.lab8_task7, name="lab8_task7"), 
    #task1 lab 11
    path('students/', views.list_students, name='list_students'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/edit/<int:id>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:id>/', views.delete_student, name='delete_student'),
    #task2
    path('Lab11_task2/', views.Lab11_task2, name='Lab11_task2'),
    path('Lab11_task2/add/', views.add_student_address, name='add_student_address'),
    path('Lab11_task2/edit/<int:id>/', views.edit_student_address, name='edit_student_address'),
    path('Lab11_task2/delete/<int:id>/', views.delete_student2, name='delete_student2'), 
    #task3
    path('photo-list/', views.photo_list, name='photo_list'),
    path('upload-photo/', views.upload_photo, name='upload_photo'),
    #lab12
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),



]

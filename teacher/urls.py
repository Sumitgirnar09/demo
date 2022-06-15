from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.teacherLogin, name="teacherLogin"),

    path('register', views.register,name='teacherRegister'),
    path('logout',views.TeacherLogout,name="TeacherLogout"),
    path('createTest',views.createTest,name="createTest"),
]

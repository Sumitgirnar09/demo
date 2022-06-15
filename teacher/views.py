from curses.ascii import HT
from email import message
import email
from http.client import HTTPResponse
import imp
from tkinter.messagebox import QUESTION
from turtle import goto
from unicodedata import name
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Teacher
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout
from exam.models import Result,Question
from student.models import Student
from exam import models as QMODEL
import datetime

# Create your views here.

def register(request):
    # print("Entered in views register function")
    if request.method=="POST":
        print("teacher request is sent", request)
        f_name=request.POST.get('f_name', '')
        l_name=request.POST.get('l_name', '')
        username=f_name+"@"+"faculty"
        email=request.POST.get('email', '')
        pass1=request.POST.get('pass1','')
        pass2=request.POST.get('pass2','')
        
       
        # if (pass1!= pass2):
        #      messages.error(request, " Passwords do not match")
        #      return redirect('home')
         
        # print(f_name,l_name,branch,email)
        teacher =Teacher(f_name=f_name,l_name=l_name,email=email)
        teacher.save()
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= f_name
        myuser.last_name= l_name
        myuser.email=email
        myuser.save()
        
        # messages.info(request, 'Your password has been changed successfully!')
        print("Teacher Form registered successfully")
        return redirect("teacherLogin")

    return render(request,"teacher/register.html")


def teacherLogin(request):
    # return render(request,"student/afterlogin.html")
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            
            login(request, user)
            # dict={name:user.name}
            # messages.success(request, "Successfully Logged In")
         
            # return render(request,"teacher/afterlogin.html")
            return render(request,"teacher/teacherAfterlogin.html")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("teacher")

    return render(request,"teacher/home.html")

def TeacherLogout(request):
    logout(request)
    # messages.success(request, "Successfully logged out")
    return redirect("teacherLogin")


def createTest(request):
    if request.method=="POST":
        question=request.POST.get('question','')
        option1=request.POST.get('option1','')
        option2=request.POST.get('option2','')
        option3=request.POST.get('option3','')
        option4=request.POST.get('option4','')
        Correct_opt=request.POST.get('CorrectOption','')
        
        new_question=Question()
        new_question.question=question
        new_question.option1=option1
        new_question.option2=option2
        new_question.option3=option3
        new_question.option4=option4
        new_question.answer="Option"+Correct_opt
        new_question.save()
        
        print("Question Created Successfully")
        
    return render(request,"teacher/createTest.html")

def display_students(request):
    stud=Student.objects.all()
    dict={}
    for student in stud:
        dict[student.f_name+student.l_name]=student.mis
    print(dict)
    
        
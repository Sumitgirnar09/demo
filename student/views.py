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
from .models import Student
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout
from exam.models import Result,Question
from student.models import Student
from exam import models as QMODEL
import datetime

# std=Result.objects.all()
# ques=Question.objects.all()
# Create your views here.

All_Question=Question.objects.all()
All_Student=Student.objects.all()
All_Result=Result.objects.all()

def home(request):
    return render(request,'student/home.html')

def register(request):
    print("Entered in views register function")
    if request.method=="POST":
        print("request is sent", request)
        f_name=request.POST.get('f_name', '')
        l_name=request.POST.get('l_name', '')
        username=f_name+"@"+"coep"
        branch=request.POST.get('branch')
        email=request.POST.get('email', '')
        mis=request.POST.get('mis','')
        pass1=request.POST.get('pass1','')
        pass2=request.POST.get('pass2','')
        
       
        # if (pass1!= pass2):
        #      messages.error(request, " Passwords do not match")
        #      return redirect('home')
         
        print(f_name,l_name,branch,email)
        student =Student(f_name=f_name,l_name=l_name,branch=branch, email=email,mis=mis)
        student.save()
        print("Model Saved")    
            
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= f_name
        myuser.last_name= l_name
        myuser.branch=branch
        myuser.email=email
        myuser.mis=mis
        myuser.save()
        
        print("data created")
        messages.info(request, 'Your password has been changed successfully!')
        # messages.success(request, " Your  has been successfully created")
        return redirect('studenthome')

    return render(request, "student/register.html")

def handeLogin(request):
    # return render(request,"student/afterlogin.html")
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            
            login(request, user)
            # dict={name:user.name}
            messages.success(request, "Successfully Logged In")
            
         
            return render(request,"student/afterlogin.html")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return redirect("home")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("home")

def display_quiz(request):

    details={"question":All_Question,"student":All_Student,"result":All_Result}
    print("user in quiz.html",request.user)
    return render(request,"student/quiz.html",details)

def test(request):
    return render(request,"student/test.html")

# @property
def result(request):
    Marks=0
    Correct=0
    Wrong=0
    # Question_details=Question.
    if request.user.is_authenticated:
        print("User is login",request.user.email)
        # Searching Student object corresponding to user
        active_student="student"
        for student in All_Student:
            if student.email==request.user.email:
                active_student=student
        print('active_student',active_student)
        # print(active_student.mis)
            
        if request.method=="POST":
            count=0;
            responses={}
            correct={}
            for q in All_Question:
                count=count+1;
                correct[count]=q.answer
                print("Actual Answer",q.answer)
                print("Written Answer",request.POST.get(q.question))
                responses[count]=request.POST.get(q.question)
                if(q.answer)==request.POST.get(q.question):
                    Correct+=1
                    Marks=Marks+5
                else:
                    Wrong+=1
          
    
            result = QMODEL.Result()
            result.student=active_student
            result.marks=Marks
            result.Correct_ques=Correct
            result.Wrong_Ques=Wrong
            # result.date=datetime.date.today()
            result.save()
            print("Model Saved Successfully")
            print(responses)
            # response_dict["question"]=All_Question,
            # questions={"questions":All_Question}
            return render(request,"student/display_result.html",context={'responses':responses,'questions':All_Question,"result":result,"correct":correct})
    
    return(HttpResponse("Works Properly"))
        
# class Result(models.Model):
#     student = models.ForeignKey(Student,on_delete=models.CASCADE)
#     Correct_ques=models.PositiveIntegerField()
#     Wrong_Ques=models.PositiveIntegerField()
#     marks = models.PositiveIntegerField()
def display_marks(request):
    if request.user.is_authenticated:
        print("User is login",request.user.email)
        # Searching Student object corresponding to user
        marks_details={'result':1,'marks':0,"wrong":0,"correct":0}
        active_student="student"
        active_result="result"
        
        for student in All_Student:
            if student.email==request.user.email:
                active_student=student
                break

        for results in All_Result:
            if results.student==active_student:
                active_result=results
                break
        marks_details["marks"]=active_result.marks
        marks_details["correct"]=active_result.Correct_ques
        marks_details["wrong"]=active_result.Wrong_Ques
        marks_details["student"]=active_student
        
        # print("marks:",active_result.marks)
            
    return render(request,"student/afterlogin.html",marks_details)
    
    
        
        
    
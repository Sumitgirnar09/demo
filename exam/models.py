from asyncio.windows_events import NULL
from cgi import test
from curses.ascii import NUL
from pyexpat import model
from statistics import mode
from django.db import models
from student.models import Student
from django.utils.timezone import now
from teacher.models import Teacher
    
class Question(models.Model):
    
    # msg_id = models.AutoField(primary_key=True,default=NULL)
    # teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,default=NULL)
    # student=models.ForeignKey(Student,on_delete=models.CASCADE,default=NULL)
    testName=models.CharField(max_length=200,default=NULL)
    marks=models.PositiveIntegerField(default=4)
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    # cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200)
 
class Test(models.Model):
    Question_test = models.ForeignKey(Question,on_delete=models.CASCADE)
    test_name=models.CharField(max_length=600)
    date = models.DateTimeField(auto_now=True,blank=True)
       
class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    Correct_ques=models.PositiveIntegerField()
    Wrong_Ques=models.PositiveIntegerField()
    marks = models.PositiveIntegerField()
    # date = models.DateTimeField(default=datetime.now, blank=True)
    date = models.DateTimeField(default=now, editable=False)



    
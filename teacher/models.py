from asyncio.windows_events import NULL
from django.db import models

# Create your models here.
class Teacher(models.Model):
    msg_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100,default="")
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email= models.CharField(max_length=70, default="")
    pass1= models.CharField(max_length=70, default="")
    pass2= models.CharField(max_length=70, default="")
    
    def __str__(self):
        return self.f_name + " " + self.l_name
import django
from django.contrib import admin

# from otp.teacher.models import Teacher
from .models import Teacher

# Register your models here.
admin.site.register(Teacher)

from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("home")
    return render(request,'home/home.html')
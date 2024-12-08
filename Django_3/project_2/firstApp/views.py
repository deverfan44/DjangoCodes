from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'test.html')

def courses(request):
    return render(request, 'firstApp/courses.html')

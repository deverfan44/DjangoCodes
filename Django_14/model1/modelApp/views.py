from django.shortcuts import render,redirect
from . import models

def home(request):
    student = models.Student.objects.all()
    # print(student)
    return render(request, './modelApp/home.html', {'data': student})

def deleteStudent(request, roll):
    std = models.Student.objects.get(pk = roll).delete()
    return redirect('homepage')
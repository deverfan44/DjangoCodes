from django.shortcuts import render

def courses(request):
    return render(request,'navhost/courses.html')

def blog(request):
    return render(request,'navhost/blog.html')
from django.shortcuts import render
from django.http import HttpResponse


def courses(request):
    return HttpResponse("Html/CSS/Javascript")
def about(request):
    return HttpResponse("This is about page")
def home(request):
    return HttpResponse("This is first app home page")
from django.shortcuts import render
from django.http import HttpResponse


def contactPage(request):
    return HttpResponse("This is Contact Page")

def home(request):
    return HttpResponse("This is home page")

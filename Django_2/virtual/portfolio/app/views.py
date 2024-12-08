from django.shortcuts import render
from django.http import HttpResponse

def courses(request):
    return HttpResponse("Html-Css-Javascritp-React-ReactNative")

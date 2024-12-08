from django.shortcuts import render

def about(request):
    return render(request, 'nevigation/about.html')

def contact(request):
    return render(request, 'nevigation/contact.html')

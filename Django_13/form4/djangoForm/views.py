from django.shortcuts import render
from . forms import userform, studentform, passwordValidationProject

def djangoform(request):
    if request.method == 'POST':
        form = userform(request.POST,request.FILES)
        if form.is_valid():
            file = form.cleaned_data['upload']
            with open('./djangoForm/upload/' + file.name , 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = userform()
    return render(request, './djangoFrom/djangoform.html', {'form':form})

def stdform(request):
    if request.method == 'POST':
        stdform = studentform(request.POST, request.FILES)
        if stdform.is_valid():
            print(stdform.cleaned_data)
    else:
        stdform = studentform()
    return render(request, './djangoFrom/studentform.html', {'stdform':stdform})

def passwordValidation(request):
    if request.method == 'POST':
        passwordform = passwordValidationProject(request.POST)
        if passwordform.is_valid():
            print(passwordform.cleaned_data)
    else:
        passwordform = passwordValidationProject()
    return render(request, './djangoFrom/password.html',{'passwordform':passwordform})
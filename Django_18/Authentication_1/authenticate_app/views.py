from django.shortcuts import render, redirect
from . forms import ResisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'home.html')

def signUP(request):
    if request.method == 'POST':
        form = ResisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account Create Successfull')
            print(form.cleaned_data)
            form.save(commit=True)
        else:
            messages.warning(request, 'Account not created')
    else:
        form = ResisterForm()
    return render(request,'signup.html', {'form':form})

def userLogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=name, password=userpass)
                if user is not None:
                    login(request,user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
    else:
        return redirect('profile')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect('login')

def userLogout(request):
    logout(request)
    return redirect('login')
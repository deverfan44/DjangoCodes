from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisteredFrom, UserChangeData
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = RegisteredFrom(request.POST)
        if form.is_valid():
            messages.success(request, 'Your Account Successfully Created')
            form.save(commit=True)
            # print(form.cleaned_data)
            return redirect('signin')
        else:
            messages.error(request, 'Your Account not Created')
    else:
        form = RegisteredFrom()
    return render(request, './authenticate_app/signup.html', {'form':form})



def signin(request):
    if request.user.is_authenticated:
        return redirect('profile')
    
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                # messages.error(request, 'Please enter right username and password')
                return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, './authenticate_app/signin.html', {'form':form})

def profile(request):
    if not request.user.is_authenticated:
        return redirect('signup')
    
    if request.method == 'POST':
        form = UserChangeData(request.POST, instance=request.user)
        if form.is_valid():
            messages.success(request, 'Your Account Successfully Updated')
            form.save(commit=True)
            # print(form.cleaned_data)
        else:
            messages.error(request, 'Your Account not Update')
    else:
        form = UserChangeData()
    return render(request, './authenticate_app/profile.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('signin')

def pass_change(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('signin')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, './authenticate_app/passchange.html', {'form':form})


# Change Password without old password

# def pass_change_2(request):
#     if request.method == 'POST':
#         form = SetPasswordForm(user=request.user, data=request.POST)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             return redirect('profile')
#     else:
#         form = SetPasswordForm(user=request.user)
#     return render(request, './authenticate_app/passchange.html', {'form':form})
        

def change_user_data(request):
    if not request.user.is_authenticated:
        return redirect('signup')
    
    if request.method == 'POST':
        form = UserChangeData(request.POST, instance=request.user)
        if form.is_valid():
            messages.success(request, 'Your Account Successfully Updated')
            form.save(commit=True)
            # print(form.cleaned_data)
        else:
            messages.error(request, 'Your Account not Update')
    else:
        form = UserChangeData()
    return render(request, './authenticate_app/profile.html', {'form':form})
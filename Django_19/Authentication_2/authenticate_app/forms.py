from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib import messages
from django import forms

class RegisteredFrom(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'required'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id':'required'}))
    class Meta:
        model = User
        fields = ['username','first_name','email']

class UserChangeData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name','email']




from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class ResisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confrim Password:')
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username','first_name','last_name','email']
        # widgets = {
        #     'email': forms.EmailField(required=True)
        # }
        labels = {
            'password1': 'Give password',
        }

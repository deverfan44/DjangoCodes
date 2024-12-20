from django import forms
import datetime


allColor = [('Red','Red'),('Blue','Blue'),('Yellow','Yellow')]
class userFroms(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Type your name'}), initial='Md ') # Charfield has a default widget TextInput
    email = forms.EmailField(label='Enter your email')
    brithday = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}), initial=datetime.date.today)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}), required=False)
    sex = forms.ChoiceField(choices=[('Male','Male'),('Female','Female')], widget=forms.RadioSelect)
    favourite_color =forms.MultipleChoiceField(choices=allColor, widget=forms.CheckboxSelectMultiple)

    
from django import forms

class userForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField(label='Are you female', required=False)
    dob = forms.DateField()
    appointment = forms.DateTimeField()
    CHOICES = [('S','Smaill'), ('M','Medium'), ('L','Large')]
    size = forms.ChoiceField(choices=CHOICES)
    pizza = forms.MultipleChoiceField(choices=[('P','Pepproni'), ('M','Masrum'), ('B','Beaf')])
    upload = forms.FileField(label='Upload your file', required=False)
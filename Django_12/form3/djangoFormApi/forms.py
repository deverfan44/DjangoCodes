from django import forms

class submitFrom(forms.Form):
    firstname = forms.CharField(label="Type your first name: ", initial='Mr ', help_text="Total lenght within 50 characters", widget=forms.TextInput({'class': 'firstclass'}))
    lastname = forms.CharField(label="Type your last name: ", required=False)
    email = forms.EmailField(help_text="Type your email", widget=forms.EmailInput({'class': 'firstemail', 'placeholder': 'Type your professional email'}),)
    age = forms.IntegerField(initial=18, disabled=True)
    height = forms.FloatField()
    # weight = forms.IntegerField()
    weight = forms.CharField(widget=forms.NumberInput)
    upload = forms.FileField()
    brithday = forms.DateField(widget=forms.DateInput(attrs = {'type' : 'date'}))
    appointment = forms.DateTimeField(widget=forms.DateTimeInput(attrs = {'type' : 'datetime-local'}))
    district = forms.ChoiceField(choices=[('Chattogram','Chattogram'),('Dhaka','Dhaka'),('Rajshahi','Rajshai'),('Sylhet','Sylhet'),('Barisal','Barisal')])
    hobby = forms.MultipleChoiceField(choices=[('Gardening','Gardening'),('Fishing', 'Fishing'),('Reading', 'Reading'),('Coding','Coding')], widget=forms.CheckboxSelectMultiple)
    size = forms.ChoiceField(
        choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')],
        widget=forms.RadioSelect
        )
    comment = forms.CharField(widget=forms.Textarea({'class': 'class1 class2', 'rows': 5}), required=False, label="Drop Your Comment")
from django import forms
from django.core import validators

class userform(forms.Form):
    name = forms.CharField(label="Enter your name", initial='Md ')
    email = forms.EmailField(label="Enter your email", widget=forms.EmailInput(attrs={'placeholder': "Type your email"}))
    age = forms.IntegerField(initial=18, disabled=True)
    sex = forms.ChoiceField(choices=[('Male','Male'),('Female','Female')], widget=forms.RadioSelect)
    upload = forms.FileField()
    hobby = forms.MultipleChoiceField(choices=[('Gardening','Gardening'),('Fishing','Fishing'),('Coding','Coding')], widget=forms.CheckboxSelectMultiple, required=False)
    comment = forms.CharField(label='Put your comment', widget=forms.Textarea(attrs={'rows':5}))


    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name within at least 10 chracter")
    #     else:
    #         return valname
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '@gmail.com' not in valemail:
    #         raise forms.ValidationError("You must add @gmail.com")
    #     else:
    #         return valemail

    #shortcut
    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        valemail = self.cleaned_data['email']

        if len(valname) < 10:
            raise forms.ValidationError("Enter a name within at least 10 chracter")
        
        if '@gmail.com' not in valemail:
            raise forms.ValidationError("You must add @gmail.com")





def len_check(val):
    if len(val) < 15:
        raise forms.ValidationError("Enter a value at least 15 chars")
    

class studentform(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(11, message='Enter your name length must be within 10 chracter')])
    email = forms.EmailField(label="Enter your email", validators=[validators.EmailValidator(message='Enter a valid email')])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(20), validators.MinValueValidator(12)])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','jpg'])])
    comment = forms.CharField(widget=forms.Textarea, validators=[len_check])

class passwordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confrim_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valpasword = cleaned_data['password']
        valconfrimpass = cleaned_data['confrim_password']
        if(len(valpasword) < 8 or len(valconfrimpass) < 8):
            raise forms.ValidationError('your password must be at least 8 lenght')
        if((valconfrimpass != valpasword)):
            raise forms.ValidationError("Your password and confrim password not match. Please same password in both field")
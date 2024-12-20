from django import forms
from modelApp.models import StudentModel

class StudentFrom(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        # exlude = []
        labels = {
            'name': 'Student Name',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Type your name'})
        }
        help_texts = {
            'father_name': 'Write your full father name'
        }
        # error_messages = {
        #     'name': {'required': 'Your name must required'}
        # }


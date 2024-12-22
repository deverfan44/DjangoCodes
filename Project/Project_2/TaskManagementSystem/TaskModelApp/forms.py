from django import forms
from TaskModelApp.models import Task

class taskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows':5}),
            'assign_date': forms.DateInput(attrs={'type': 'date'}),
        }

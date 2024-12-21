from django import forms
from musicianApp.models import musicianModel

class musicianFrom(forms.ModelForm):
    class Meta:
        model = musicianModel
        fields = '__all__'
        widgets = {
            'instrument': forms.Textarea(attrs={'rows':3})
        }
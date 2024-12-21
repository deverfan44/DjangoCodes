from django import forms
from album.models  import albumModel
rating = (("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")) 
class albumFrom(forms.ModelForm):
    class Meta:
        model = albumModel
        fields = '__all__'
        widgets = {
            'rating': forms.RadioSelect(choices=rating)
        }

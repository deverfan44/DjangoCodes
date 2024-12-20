from django import forms
from .models import Post

class PostFrom(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
    

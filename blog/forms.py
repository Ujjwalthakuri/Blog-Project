from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = postModel
        fields = ['title', 'content']

class PostUpdateForm(forms.ModelForm):
    class Meta: 
        model = postModel
        fields = ['title', 'content']
# forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

# Inheritating form for updating profile
class userUpdateForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(userUpdateForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'email']:
            self.fields[fieldname].help_text = None

    
class ProfileUpdateForm(forms.ModelForm):
    class Meta: 
        model = profileModel
        fields = ['image']
# Inheritating form for updating profile
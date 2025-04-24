from django import forms
from .models import *

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    class Meta:
        model = postModel
        fields = ['title', 'content']

class PostUpdateForm(forms.ModelForm):
    class Meta: 
        model = postModel
        fields = ['title', 'content']
        
class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Add a comment...'}))
    class Meta:
        model = Comment
        fields = ('content',)
      
    #   search + filter  
class PostFilterForm(forms.Form):
    title = forms.CharField(required=False, label="Title")
    category = forms.ModelChoiceField(queryset=CategoryModel.objects.all(), required=False)
    author = forms.CharField(required=False)
    # tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    # end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = CategoryModel
        fields = ('name',)
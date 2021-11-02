from django import forms
from . models import Post
class AddForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['posted']
        context_object_name = 'form'
    

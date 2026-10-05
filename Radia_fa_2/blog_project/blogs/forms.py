from django import forms 
from blogs.models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = '__all__'
        
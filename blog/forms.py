from django import forms

from .models import BlogPost


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['author', 'title', 'text', 'status']

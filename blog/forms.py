from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    Choice=(('PUBLIC', 'public'), ('PRIVATE', 'private'))
    category=forms.ChoiceField(choices=Choice)
    
    class Meta:
        model=Post
        fields=['title', 'content','image','category', ]
    
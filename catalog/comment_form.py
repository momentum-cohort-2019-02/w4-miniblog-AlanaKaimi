import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import BlogPost, Comment

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('user', 'body',)


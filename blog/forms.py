from django import forms
from django.forms import fields
from blog.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {
            'comment',  # 受け入れる model を記載
        }

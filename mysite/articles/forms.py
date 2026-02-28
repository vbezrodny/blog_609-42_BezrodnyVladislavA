from django import forms

from . import views
from . import models


class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'thumbnail']
        labels = {
            "title": "Заголовок",
            "body": "Содержание",
            "thumbnail": "Вложение",
        }
        widgets = {
            "title": forms.TextInput(attrs={'placeholder': 'Напишите заголовок статьи...'}),
            "body": forms.Textarea(attrs={'placeholder': 'Напишите содержание для статьи...'}),
            "thumbnail": forms.ClearableFileInput(),
        }

from django import forms
from article.models import Article

class ArticleForm(forms.ModelForm):
    author = forms.CharField(widget = forms.HiddenInput(), required = False)
    title = forms.CharField(required = True)
    class Meta:
        model = Article
        fields = ('title', 'description')
        labels = {
            'title': 'Заголовок',
            'description': 'Опис',
        }
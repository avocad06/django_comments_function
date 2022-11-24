from django import forms
from .models import Article, Comment
from .widgets import CounterTextInput

class NewPostForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ("title", "content", "image",)
        
class NewCommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ("content",)
        labels = {
            'content' : '',
        }
        widgets = {
            'content' : CounterTextInput(attrs={'class': 'form-control', 'title': 'Your name'})
        }

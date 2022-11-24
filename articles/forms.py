from django import forms
from .models import Article, Comment
from .widgets import CounterTextInput, PreviewImageWidget

class NewPostForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ("title", "content", "image",)
        widgets = {
            'image' : PreviewImageWidget,
        }
        
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

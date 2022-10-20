from cProfile import label
from django import forms
from .models import Article, Comment

class NewPostForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ("title", "content",)
        
class NewCommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ("content",)
        labels = {
            'content' : '',
        }

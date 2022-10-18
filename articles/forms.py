from django import forms
from .models import Article, Comment

class NewPostForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = "__all__"
        
class NewCommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ("content",)

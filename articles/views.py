from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import NewPostForm, NewCommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        "articles" : articles,
    }
    return render(request, "articles/index.html", context)

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = NewCommentForm()
    context = {
        "article" : article,
        "form" : comment_form, 
    }
    return render(request, "articles/detail.html", context)

def create(request):
    if request.method == "POST":
        forms = NewPostForm(request.POST)
        if forms.is_valid():
            forms.save()
            pk = Article.objects.all(-pk)[0]
            return redirect('articles:detail', pk)
    
    else:
        forms = NewPostForm
    context = {
        "forms" : forms,
    }
    return render(request, 'articles/create.html', context)

def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = NewCommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)

def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
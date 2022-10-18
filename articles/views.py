from django.shortcuts import render, redirect
from .models import Article
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
    context = {
        "article" : article,
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
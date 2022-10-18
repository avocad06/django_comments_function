from django.shortcuts import render
from .models import Article

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
    
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import NewPostForm, NewCommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

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
    comments = article.comment_set.all()
    context = {
        "article" : article,
        "form" : comment_form, 
        "comments" : comments,
    }
    return render(request, "articles/detail.html", context)

def create(request):
    if request.method == "POST":
        # 이미지 파일- request.FILES 객체로 전달
        # 폼에 넣으려면 인수로 전달
        forms = NewPostForm(request.POST, request.FILES)
        if forms.is_valid():
            article = forms.save(commit=False)
            article.user = request.user
            article.save()
            pk = Article.objects.order_by("-pk")[0].pk
            return redirect('articles:detail', pk)
    
    else:
        forms = NewPostForm
    context = {
        "forms" : forms,
    }
    return render(request, 'articles/create.html', context)

@login_required
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = NewCommentForm(request.POST)
    if comment_form.is_valid():
        # 이 시점에는 모델'폼'의 인스턴스, 객체를 반환
        comment = comment_form.save(commit=False)
        # 이 시점에서는 '모델'의 인스턴스를 반환
        comment.article_id = article.pk
        comment.save()
        context = {
            # json으로 응답할 때 담아갈 변수
            'content' : comment.content,
            'userName' : comment.user.username,
        }
        return JsonResponse(context)
    # 요청이 GET으로 들어오든 POST로 들어오든 게시물 상세페이지로 리디렉트
    # GET으로 들어온다면 46번째 코드까지는 실행(유효성 검사 NOT NULL 탈락)
    # return redirect('articles:detail', article.pk)
    

@login_required
def comment_delete(request, article_pk, comment_pk):
    # 요청한 유저와 게시글 작성자의 pk가 일치해야 한다.
    article = Article.objects.get(pk=article_pk)
    if request.user == article.user:
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
        return redirect('articles:detail', article_pk)
    else:
        return HttpResponseForbidden()

# 좋아요 기능 구현
def like(request, article_pk):
    # 일단 좋아요를 누른 게시글의 article을 가져온다.
    article = get_object_or_404(Article, pk=article_pk)
    # 만약 이 게시글을 누른 사용자 중에 유저가 있다면,
    if article.like_users.filter(pk=request.user.pk).exists():
        # 유저를 지우고,
        article.like_users.remove(request.user)
    
    # 유저가 없다면,
    else:
        # 좋아요에 유저를 추가한다.
        article.like_users.add(request.user)
    return redirect('articles:detail', article_pk)
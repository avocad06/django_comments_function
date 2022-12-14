from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, JsonResponse
from .forms import SignoutForm

# Create your views here.
def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            forms = AuthenticationForm(request, data=request.POST)
            if forms.is_valid():
                auth_login(request, forms.get_user())
                return redirect(request.GET.get('next') or "articles:index")
    
        else:
            forms = AuthenticationForm()
        context = {
            "forms" : forms,
        }
        return render(request, "accounts/login.html", context)
    
    else:
        return HttpResponseForbidden()

def logout(request):
    auth_logout(request)
    return redirect("articles:index")

def detail(request, user_pk):
    us = get_user_model().objects.get(pk=user_pk)
    return render(request, "accounts/detail.html", {"us": us})

# 회원가입 함수
def signout(request):
    if not request.user.is_authenticated: 
        if request.method == "POST":
            # 회원가입 폼이 필요
            forms = SignoutForm(request.POST)
            if forms.is_valid():
                # 객체를 반환
                user = forms.save()
                # 모델의 인스턴스 = User클래스로 생성한 객체(인스턴스)
                # 로그인 함수에 필요한 것은 http객체와 user객체
                auth_login(request, user)
                return redirect("articles:index")
            
        else:
            forms = SignoutForm()
            context = {
                "forms" : forms,
            }
        return render(request, "accounts/signout.html", context)
    
    else:
        return HttpResponseForbidden()

@login_required
def follow(request, user_pk):
    user = get_user_model()
    us = get_object_or_404(user, pk=user_pk)

    if not request.user == us:
        if request.user in us.follower.all():
            print("no")
            us.follower.remove(request.user)
            is_followed = False
        else:
            print("yes")
            us.follower.add(request.user)
            is_followed = True
        followers = us.follower.all()
        print(followers)
        # 팔로워들을 담을 변수
        followers_all = []
        for follower in followers:
            followers_all.append({
                "follower": follower.username,
                "follower_pk" : follower.pk
                })
            print(followers_all)
        return JsonResponse({"is_followed": is_followed,
                             "follower_count" : us.follower.count(),
                             "followers_all" : followers_all,})
    else:
        return HttpResponseForbidden()
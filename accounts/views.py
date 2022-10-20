from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseForbidden
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
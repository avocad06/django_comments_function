from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseForbidden

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
    return render(request, "accounts/detail.html")
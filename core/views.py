from django.shortcuts import render
from .forms import UniversityForm

# Create your views here.
def new(request):
    form = UniversityForm()
    context = {
        "form" : form,
    }
    return render(request, "core/new.html", context)
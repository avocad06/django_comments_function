from django.contrib import admin
from .models import University, Student
from .forms import UniversityForm

@admin.register(University)
class CountryAmin(admin.ModelAdmin):
    form = UniversityForm


@admin.register(Student)
class PostAmin(admin.ModelAdmin):
    pass
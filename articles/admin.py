from django.contrib import admin
from .models import Article, Comment
from .forms import NewCommentForm

@admin.register(Article)
class CountryAmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class PostAmin(admin.ModelAdmin):
    form = NewCommentForm
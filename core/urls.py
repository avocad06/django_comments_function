from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path("new/", views.new, name="new")
]

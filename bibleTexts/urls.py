from django.urls import re_path
from . import views


urlpatterns = [
    re_path("create_text", views.create_text),
    re_path("take_text", views.take_text)
]
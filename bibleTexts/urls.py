from django.urls import re_path, path
from . import views


urlpatterns = [
    re_path("create_text", views.create_text),
    re_path("take_text", views.take_text),
    path("conclude_devotional/<int:devotionalPk>/", views.conclude_devotional)
]
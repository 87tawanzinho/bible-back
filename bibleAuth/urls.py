from django.urls import path, re_path
from . import views 

urlpatterns = [
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('test_token', views.test_token),
    path('toggle_card/<str:chapter>/<int:card_id>/', views.completed_this_card)
]
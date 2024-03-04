from django.urls import path, re_path
from . import views 

urlpatterns = [
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('test_token', views.test_token),
    re_path('change_warn', views.change_warn),
    re_path('take_user_data', views.take_user_data),
    path('toggle_card/<str:chapter>/<int:card_id>/', views.completed_this_card),
    path('take_cards/', views.take_cards)
]
# accounts/urls.py
from django.urls import path
from .import views
from .views import *

urlpatterns = [
    path("", login_view, name="login"),
    path("signup/", views.signup, name="signup"),
    path('profile/<int:id>/', views.profile, name='profile'),
    path('edit_profile/<int:id>/', views.edit_profile, name='edit_profile'),
]

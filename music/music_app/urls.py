# accounts/urls.py
from django.urls import path
from .import views
from .views import *

urlpatterns = [
    path("", login_view, name="login"),
    path("signup/", views.signup, name="signup"),
]

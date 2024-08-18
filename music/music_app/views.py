# accounts/views.py
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import *



def login_view(request):
    form = LoginForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect("home")

    return render(request, "login/login.html", {"form": form})


def signup(request):
    form = SignupForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("home")

    return render(request, "login/signup.html", {"form": form})

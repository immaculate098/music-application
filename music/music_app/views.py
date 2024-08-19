# accounts/views.py
from django.contrib.auth import login
from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from .models import *



def login_view(request):
    form = LoginForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect("home")

    return render(request, "music_app/login.html", {"form": form})


def signup(request):
    form = SignupForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("home")

    return render(request, "music_app/signup.html", {"form": form})


def profile(request, id):
    profile = Signup.objects.get(id=id)  
    return render(request, 'music_app/profile.html', {'profile': profile})  


def edit_profile(request, id):
    profile = get_object_or_404(Signup, id=id) 
    if request.method == 'POST':
        form = SignupForm(request.POST, instance=profile)  
        if form.is_valid():
            form.save()  
            return redirect('profile')  
        else:
            print("Form is not valid")
    else:
        form = SignupForm(instance=profile)  
    return render(request, 'music-app/edit_profile.html', {'form': form, 'profile': profile})  

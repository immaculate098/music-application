from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import SignupForm, LoginForm
from .models import Signup
from django.contrib.auth.models import User, auth

# def login(request):
#     form = LoginForm(data=request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         user = form.get_user()
#         if user:
#             login(request, user)
#             return redirect("edit_profile")
#         else:
#             form.add_error(None, "Invalid username or password")

#     return render(request, "musicApp/login.html", {"form": form})

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)  
        if form.is_valid():
            form.save()  
            return redirect('home')  
        else:
            print("Form is not valid")  
        form = LoginForm() 
    return render(request, 'musicApp/profile.html', {'form': form}) 
                


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)  
        if form.is_valid():
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["confirm_password"]
            if password == confirm_password:
                form.save()  
                return redirect('login')  
        else:
            print("Form is not valid")  
    else:
        form = SignupForm() 
    return render(request, 'musicApp/signup.html', {'form': form}) 



def profile(request, id):
    profile = Signup.objects.get(id=id)  
    return render(request, 'musicApp/profile.html', {'profile': profile})  

# def profile(request):
#     return render(request, 'musicApp/profile.html')


def edit_profile(request, id):
    profile = get_object_or_404(Signup, id=id) 
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES, instance=profile)  
        if form.is_valid():
            form.save()  
            return redirect('profile', id=profile.id)  
    else:
        form = SignupForm(instance=profile)  
    return render(request, 'musicApp/edit_profile.html', {'form': form, 'profile': profile})


# def edit_profile(request):
#     return render(request, 'musicApp/edit_profile.html')

def downloads(request):
    return render(request, 'musicApp/downloads.html')

def albums(request):
    return render(request, 'musicApp/albums.html')

def playlists(request):
    return render(request, 'musicApp/playlists.html')

def favorites(request):
    return render(request, 'musicApp/favourites.html')
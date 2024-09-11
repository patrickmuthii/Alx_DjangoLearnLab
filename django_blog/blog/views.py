from django.shortcuts import render, redirect
from . import views
from .models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django import forms
from django.contrib.auth.forms import UserChangeForm
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, form.instance)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'blog/register.html', {'form': form})  
@login_required
def profile_view(request): 
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})        

def posts_view(request):
    return render(request, 'blog/posts.html')

def home_view(request):
    return render(request, 'blog/base.html')
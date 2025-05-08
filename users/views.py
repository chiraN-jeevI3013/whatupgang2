from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from teams.models import Team

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # just for learning
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password1 = form.cleaned_data.get("password1")
            password2 = form.cleaned_data.get("password2")

            user = form.save()  
            messages.success(request, f"Account created for {user.username}. Please log in.")
            # Log user cred
            print("User created successfully: Username:: ", username)
            print("User created successfully: Email:: ", email)
            print("User created successfully: Password1:: ", password1)
            print("User created successfully: Password2:: ", password2)
            # Send welcome email
            user.email_user(
                subject="Welcome to WhatUpGang!",
                message="Hello Admin, welcome to WhatUpGang, your 1 stop destination for managing your team!"
            )
            return redirect('login')
        else:
            # Form is invalid
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required(login_url='login')
def home_view(request):
    teams = Team.objects.filter(created_by=request.user)
    return render(request, 'teams/home.html', {'teams': teams})

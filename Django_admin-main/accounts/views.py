from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User

def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists. Please login.")
            return redirect('login')
        
        user = User.objects.create_user(email=email, name=name, password=password)
        login(request, user)
        messages.success(request, "Signup successful!")
        return redirect('home')
    return render(request, 'accounts/signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.name}!")
            return redirect('home')
        else:
            if not User.objects.filter(email=email).exists():
                messages.error(request, "Email does not exist, please signup.")
            else:
                messages.error(request, "Invalid password.")
            
    return render(request, 'accounts/login.html')

def home_view(request):
    return render(request, 'accounts/home.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Logged out successfully.")
    return redirect('login')

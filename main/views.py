from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

# User Registration View
def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists!")

        # Create a regular user
        User.objects.create_user(username=username, email=email, password=password)
        return HttpResponse("Registration successful! You can now log in.")
    return render(request, 'register.html')

# User Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard
        else:
            return HttpResponse("Invalid credentials!")
    return render(request, 'login.html')

# User Logout View
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

# Superuser Creation View (Only Superusers)
@user_passes_test(lambda u: u.is_superuser)
def create_superuser_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not email or not password:
            return HttpResponse("All fields are required!")
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists!")

        User.objects.create_superuser(username=username, email=email, password=password)
        return HttpResponse("Superuser created successfully!")
    return render(request, 'create_superuser.html')

# Dashboard View

def dashboard_view(request):
    return render(request, 'dashboard.html', {'user': request.user})

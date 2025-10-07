#from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')
# 1️⃣ Custom Registration Form
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# 2️⃣ Register View
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect("profile")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})

# 3️⃣ Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect("profile")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "blog/login.html")

# 4️⃣ Logout View
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("login")

# 5️⃣ Profile View
@login_required
def profile_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        request.user.email = email
        request.user.save()
        messages.success(request, "Profile updated successfully.")
        return redirect("profile")
    return render(request, "blog/profile.html")
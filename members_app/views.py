from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUser


def signup_user(request):
    form = RegisterUser(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                password = form.password_clean()
                email = form.email_clean()
                form.save()
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
            except ValidationError as e:
                messages.error(request, e.message)
        else:
            messages.error(request, "All fields are required")
    return render(request, 'authenthication/signup.html', {'form': form, 'signup': 'signup'})


def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        messages.error(request, "Invalid login/password")
        return redirect('login_user')
    else:
        return render(request, 'authenthication/loginpage.html', {'login': 'login'})


def logout_user(request):
    logout(request)
    messages.success(request, "Successfully loggedout")
    return redirect('login_user')

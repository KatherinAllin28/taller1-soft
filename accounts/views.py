from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .models import UserProfile  # Import your custom user model
from .services.django_auth_service import DjangoAuthService

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect('/')
            except IntegrityError:
                form.add_error(None, "A user with that username already exists.")
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def logoutaccount(request):
    logout(request)
    return redirect('/')

auth_service = DjangoAuthService()

def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'loginaccount.html', {'form': AuthenticationForm()})
    else:
        user = auth_service.authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'loginaccount.html', {
                'form': AuthenticationForm(), 
                'error': 'Username and password do not match'
            })
        else:
            login(request, user)
            return redirect('/')

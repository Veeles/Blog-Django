from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.shortcuts import redirect
from django.contrib import messages


def user_login(request):
    pass

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration sucessful. ')
            return redirect('/')
    form = RegisterForm()
    return render(request, 'register.html', {'form': form})

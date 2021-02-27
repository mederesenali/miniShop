from pyexpat.errors import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from users.forms import RegisterForm


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("login")
    else:
        form = RegisterForm()

    return render(response, "registration/register.html", {"form": form})


@login_required
def profile(request):
    return render(request, 'registration/profile.html')


def logoutUser(request):
    logout(request)
    return redirect('login')

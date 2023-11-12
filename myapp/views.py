from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

# Create your views here.



def register_request(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, 'registration/registration.html', {"form": form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {"form": form})

def logout_request(request):
    logout(request)
    return redirect("home")

@login_required(login_url="/login")
def restricted_page(request):
    return render(request, 'registration/restricted_page.html')

def home(request):
    return render(request, 'registration/home.html')
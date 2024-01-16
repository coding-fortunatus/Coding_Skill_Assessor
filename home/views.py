from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.


def homePage(request):
    return render(request, 'assessor/home.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, template_name='assessor/register.html', context={'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Update with your actual home URL
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, template_name='assessor/login.html', context={'form': form})


def test(request):
    return render(request, template_name="assessor/test.html")

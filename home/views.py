from django.shortcuts import render

# Create your views here.


def homePage(request):
    return render(request, 'assessor/home.html')


def register(request):
    return render(request, 'assessor/register.html')


def login(request):
    return render(request, 'assessor/login.html')


def test(request):
    return render(request, template_name="test.html")

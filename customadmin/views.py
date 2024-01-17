from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home.models import Language
from django.contrib.auth.models import User
# Create your views here.


@login_required(redirect_field_name="login")
def dashboard(request):

    return render(request, template_name='custom/dashboard.html')


@login_required(redirect_field_name="login")
def allUser(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, template_name='custom/users.html', context=context)

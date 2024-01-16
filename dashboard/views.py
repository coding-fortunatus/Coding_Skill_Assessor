from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home.models import Language

# Create your views here.


@login_required(redirect_field_name="login")
def app(request):
    return render(request, template_name='students/home.html')


@login_required(redirect_field_name="login")
def test(request, slug):
    language = Language.objects.get(slug=slug)

    context = {
        'language': language
    }
    return render(request, template_name='students/test.html', context=context)

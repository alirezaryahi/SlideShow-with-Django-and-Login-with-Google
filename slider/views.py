from django.shortcuts import render, redirect
from .models import Slider
from django.contrib.auth import logout
from django.utils.translation import activate

# Create your views here.


def home(request):
    slides = Slider.objects.filter(status=True, article__status=True)
    context = {
        'slides': slides
    }
    return render(request, 'slideShow.html', context)


def log_out(request):
    logout(request)
    return redirect(request.GET.get('next'))


def change_lang(request):
    activate(request.GET.get('lang'))
    return redirect(request.GET.get('next'))


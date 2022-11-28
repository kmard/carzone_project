from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    team = Team.objects.all()
    data = {
        'teams':team,
    }
    return render(request, 'pages/home.html',data)
def about(request):
    team = Team.objects.all()
    data  = {
        'teams':team,
    }
    return render(request, 'pages/about.html', data)
def contact(request):
    return render(request, 'pages/contact.html', {})
def services(request):
    return render(request, 'pages/services.html', {})

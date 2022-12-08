from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from cars.models import *

# Create your views here.
def home(request):
    team = Team.objects.all()
    featured_cars = Car.objects.order_by("-created_date").filter(is_featured=True)
    all_cars = Car.objects.order_by("created_date")
    data = {
        'teams':team,
        'featured_cars':featured_cars,
        'all_cars':all_cars,
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

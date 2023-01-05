from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from carzone import settings
from .models import *
from cars.models import *

# Create your views here.
def home(request):
    team = Team.objects.all()
    featured_cars = Car.objects.order_by("-created_date").filter(is_featured=True)
    all_cars = Car.objects.order_by("created_date")
    model_search = Car.objects.values_list('model',flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    data = {
        'teams':team,
        'featured_cars':featured_cars,
        'all_cars':all_cars,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
    }
    return render(request, 'pages/home.html',data)
def about(request):
    team = Team.objects.all()
    data  = {
        'teams':team,
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html', {})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # admin_info = User.objects.get(is_superuser=True).email
        # send_mail(
        #     f'{name} / {subject} / {phone} ',
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [email,admin_info],
        #     fail_silently=False,
        # )

        messages.success(request,'Thank you for contact us')

        return redirect('contact')

    return render(request, 'pages/contact.html', {})
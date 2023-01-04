from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from carzone import settings
from contacts.models import Contact
from django.core.mail import send_mail


def inquiry(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        customer_need = request.POST.get('customer_need')
        car_id = request.POST.get('car_id')
        car_title = request.POST.get('car_title')
        city = request.POST.get('city')
        state = request.POST.get('state')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        if request.user.is_authenticated:
            user_id = request.POST.get('user_id')
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry about this car. Please wait answer.')
                return redirect('/cars/' + car_id)

        contact = Contact(car_id=car_id, user_id=user_id, first_name=first_name,
                          last_name=last_name, customer_need=customer_need,
                          city=city, state=state, email=email, phone=phone,
                          message=message, car_title=car_title)

        # admin_info = User.objects.get(is_superuser=True).email
        # send_mail(
        #     'New Car Inquiry',
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     ['to@example.com',admin_info],
        #     fail_silently=False,
        # )

        contact.save()
        messages.success(request, 'Your request has been submitted, we will back to you soon')
        return redirect('/cars/' + car_id)

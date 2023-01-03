from django.contrib import messages
from django.shortcuts import render, redirect
from contacts.models import Contact

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

        contact = Contact(car_id=car_id, user_id=user_id,first_name =first_name,
                          last_name = last_name,customer_need = customer_need,
                          city = city,state = state,email = email,phone = phone,
                          message = message,car_title = car_title)
        contact.save()
        messages.success(request,'Your request has been submitted, we will back to you soon')
        return redirect('/cars/'+car_id)


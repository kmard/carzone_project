from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages, auth
from contacts.models import Contact


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)

        if user:
            auth.login(request,user)
            messages.success(request,' You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, ' Invalid login credential')
            return redirect('login')
    return render(request, "accounts/login.html")

def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password.strip() == confirm_password.strip():
            if User.objects.filter(username=username).exists():
                messages.error(request, f'{username} : is exist')
                return redirect('register')
            else:
                 if User.objects.filter(email=email).exists():
                     messages.error(request, f'{email} : is exist')
                     return redirect('register')
                 else:
                     user = User.objects.create_user(
                         first_name = firstname,
                         last_name = lastname,
                         username = username,
                         email = email,
                         password = password
                     )
                     auth.login(request,user)
                     messages.success(request, f'{username} : sucessfully logged')
                     return redirect('dashboard')
                     user.save()
                     messages.success(request, f'{username} : sucessfully regstered')
                     return redirect('login')

        else:
            messages.error(request, 'Different passwords')
            return redirect('register')
    else:
        return render(request, "accounts/register.html")

@login_required(login_url = 'login')
def dashboard(request):
    user_inquiry = Contact.objects.order_by("-create_date").filter(user_id = request.user.id)
    data = {
        'inquiries':user_inquiry
    }
    return render(request, "accounts/dashboard.html",data)

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        # messages.success(request, 'You are log out.')
        return redirect('home')

    return redirect('home')
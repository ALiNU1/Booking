from django.shortcuts import render, redirect
from apps.settings.models import Setting
from .models import User
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

# Create your views here.
def register(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            user = User.objects.create(username = username,first_name = first_name, last_name = last_name,  email = email)
            user.set_password(password1)
            user.save()
            user = User.objects.get(username = username)
            user = authenticate(username = username, password = password1)
            login(request, user)
            return redirect('index')
           
        else:
            return HttpResponse("Пароли не совпадают")

    context = {
        'setting' : setting,
    }
    return render(request, 'booking/register.html', context)

def profile(request):
    setting = Setting.objects.latest('id')
    user = User.objects.all()
     
    context = {
        'setting' : setting,
        'user' : user,
    }
    return render(request,'booking/my_account.html', context)
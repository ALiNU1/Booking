from django.shortcuts import render
from apps.settings.models import Setting
from .models import Car

# Create your views here.
def car(request):
    setting = Setting.objects.latest('id')
    cars = Car.objects.all()

    context = {
        'setting' : setting,
        'cars' : cars,
    }
    return render(request,'booking/car_rentals.html',context)
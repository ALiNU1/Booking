from django.shortcuts import render
from .models import Flight
from apps.settings.models import Setting

# Create your views here.
def reis(request):
    setting = Setting.objects.latest('id')
    country = Flight.objects.all()

    context = {
        'setting' : setting,
        'country' : country,
    }
    return render(request,'booking/flights.html',context)
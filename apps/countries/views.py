from django.shortcuts import render
from .models import Flight
from apps.settings.models import Setting

# Create your views here.
def reis(request):
    setting = Setting.objects.latest('id')
    countries = Flight.objects.all()

    context = {
        'setting' : setting,
        'countries' : countries,
    }
    return render(request,'booking/flights.html',context)
from django.shortcuts import render
from .models import Flight
from apps.settings.models import Setting
from apps.hotels.models import Hotels

# Create your views here.
def reis(request):
    setting = Setting.objects.latest('id')
    countries = Flight.objects.all()
    context = {
        'setting' : setting,
        'countries' : countries,
    }
    return render(request,'booking/flights.html',context)

def reis_details(request,id):
    setting = Setting.objects.latest('id')
    country = Flight.objects.get(id=id)
    otel = Hotels.objects.order_by('?')
    context = {
        'setting' : setting,
        'country' : country,
        'otel' : otel,
    }
    return render(request,'booking/location.html',context)
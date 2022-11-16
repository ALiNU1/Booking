from django.shortcuts import render
from .models import Setting
from apps.hotels.models import Hotels

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    hotels =  Hotels.objects.all()
    context = {
        'setting' : setting,
        'hotels' : hotels,
    }
    return render(request, 'booking/index.html', context)
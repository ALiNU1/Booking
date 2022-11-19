from django.shortcuts import render
from apps.settings.models import Setting
from .models import Cruises

# Create your views here.
def cruise(request):
    setting = Setting.objects.latest('id')
    cruises = Cruises.objects.all()

    context = {
        'setting' : setting,
        'cruises' : cruises,
    }
    return render(request,'booking/cruises.html',context)
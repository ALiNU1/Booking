from django.shortcuts import render
from apps.settings.models import Setting
from .models import Hotels,HotelImage
from django.db.models import Q

# Create your views here.
def hotel_details(request, id):
    setting = Setting.objects.latest('id')
    hotel = Hotels.objects.get(id=id)
    hotel_image = HotelImage.objects.all().filter(hotel = hotel)

    context = {
        'setting' : setting,
        'hotel' : hotel,
        'hotel_image' : hotel_image,
    }
    return render(request,'booking/hotel.html', context)

def hotel_search(request):
    setting = Setting.objects.latest('id')
    hotels = Hotels.objects.all()
    qury_object = request.GET.get('key')
    if qury_object:
        hotels = Hotels.objects.filter(Q(name__icontains = qury_object))
    context = {
        'setting' : setting,
        'hotels' : hotels,
        
    }
    return render(request,"booking/search_results.html", context)

def all_hotels(request):
    setting = Setting.objects.latest('id')
    hotels = Hotels.objects.all()

    context = {
        'setting' : setting,
        'hotels' : hotels,
    }
    return render(request,'booking/hotels.html', context)
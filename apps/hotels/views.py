from django.shortcuts import render
from apps.settings.models import Setting
from .models import Hotels,HotelImage

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
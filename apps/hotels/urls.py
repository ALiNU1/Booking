from django.urls import path
from .views import hotel_details,hotel_search,all_hotels

urlpatterns = [ 
    path('hotel-details/<int:id>/',hotel_details,name='hotel_details'),
    path('search/',hotel_search,name="search"),
    path('hotels-grid/',all_hotels,name='all_hotels'),
]
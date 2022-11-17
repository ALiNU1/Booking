from django.urls import path
from .views import hotel_details,hotel_search

urlpatterns = [ 
    path('hotel_details/<int:id>/',hotel_details,name='hotel_details'),
    path('search/',hotel_search,name="search"),
]
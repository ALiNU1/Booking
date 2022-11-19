from django.urls import path
from .views import cruise

urlpatterns = [ 
    path('cruise/',cruise,name='cruise'),
]
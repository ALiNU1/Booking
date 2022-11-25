from django.urls import path
from .views import reis,reis_details

urlpatterns = [ 
    path('flights/',reis,name='reis'),
    path('flights-detail/<int:id>/',reis_details,name='reis_detail'),
]
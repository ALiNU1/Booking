from django.urls import path
from .views import reis

urlpatterns = [ 
    path('flights/',reis,name='reis'),
]
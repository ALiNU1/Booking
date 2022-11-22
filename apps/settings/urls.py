from django.urls import path
from .views import index,contact,thank_you

urlpatterns = [
    path('',index,name="index"),
    path('contact/',contact,name='contact'),
    path('thank_you/',thank_you,name='thank_you')
]
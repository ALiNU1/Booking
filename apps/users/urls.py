from django.urls import path 
from apps.users.views import register,profile,login

urlpatterns = [
    path('register/', register,name="register"),
    path('profile/',profile,name="profile"),
    path('login/',login,name='login'),
]
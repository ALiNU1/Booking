from django.urls import path 
from apps.users.views import register,profile,login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', register,name="register"),
    path('profile/<int:id>/',profile,name="profile"),
    path('login/',login,name='login'),
    path('logout/', LogoutView.as_view(next_page = 'index'), name="logout"),
]
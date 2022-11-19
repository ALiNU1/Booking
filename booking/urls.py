from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.settings.urls')),
    path('users/',include('apps.users.urls')),
    path('hotels/',include('apps.hotels.urls')),
    path('countries/',include('apps.countries.urls')),
    path('cruises/',include('apps.cruises.urls')),
    path('cars/',include,('apps.cars.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
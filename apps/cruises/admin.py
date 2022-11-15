from django.contrib import admin
from .models import Cruises,CruisePhoto

# Register your models here.
admin.site.register(Cruises)
admin.site.register(CruisePhoto)

class CruisesoAdmin(admin.TabularInline):
    model= Cruises
    extra = 5
class CruisePhotoAdmin(admin.TabularInline):
    model= CruisePhoto
    extra = 5
class CruisePhotos(admin.ModelAdmin):
    inlines = [CruisePhoto, Cruises]
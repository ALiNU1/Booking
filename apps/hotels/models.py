from django.db import models

# Create your models here.
class Hotels(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to= "cruises_image/")
    place = models.CharField(max_length=255)
    rooms = models.CharField(max_length=100)
    best = models.BooleanField(default=False)
    sale = models.IntegerField()
    price = models.IntegerField()
    airplane_prices = models.BigIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Отель"
        verbose_name_plural = "Отели"
        
class HotelImage(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    image = models.ImageField(upload_to='hotel_images/')
    hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'Дополнительноe фото'
        verbose_name_plural = 'Дополнительные фотографии'
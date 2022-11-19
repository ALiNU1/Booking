from django.db import models

# Create your models here.

class Cruises(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    poster = models.ImageField('cruiese/')
    place = models.CharField(max_length=100)
    rate = models.CharField(max_length=100)
    price = models.BigIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Круиз'
        verbose_name_plural = 'Круизы'

class CruisePhoto(models.Model):
    cruise = models.ForeignKey(Cruises,on_delete=models.CASCADE,related_name="cruisephoto",null = True,blank = True)
    photo = models.ImageField(upload_to='cruises/')


    class Meta:
        verbose_name = "Круиз фото"
        verbose_name_plural = "Фото круиза"
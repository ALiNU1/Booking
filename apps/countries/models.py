from django.db import models

# Create your models here.
class Flight(models.Model):
    title = models.CharField(max_length=255)
    price = models.BigIntegerField()
    photo = models.ImageField(upload_to='flights/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рейс'
        verbose_name_plural = 'Рейсы'
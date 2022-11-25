from django.db import models

# Create your models here.
class Flight(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    sovereign_state = models.CharField(max_length=150)
    country = models.CharField(max_length=200)
    area = models.CharField(max_length=100)
    language = models.CharField(max_length=150)
    currency = models.CharField(max_length=50)
    visa = models.CharField(max_length=100)
    price = models.BigIntegerField()
    photo = models.ImageField(upload_to='flights/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рейс'
        verbose_name_plural = 'Рейсы'
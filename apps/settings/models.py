from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название сайта")
    description = models.TextField(verbose_name="Описание сайта")
    address = models.CharField(max_length=170)
    logo = models.ImageField(upload_to = 'logo/', verbose_name="Логотип сайта")
    second_logo= models.ImageField(upload_to= 'second_logo/', verbose_name="second logo")
    phone = models.CharField(max_length=255, verbose_name="Телефонный номер")
    email = models.EmailField(max_length=150, verbose_name="Электронная почта сайта")
    facebook = models.URLField(blank = True, null=True, verbose_name="Ссылка на facebook")
    youtube = models.URLField(blank = True, null=True, verbose_name="Ссылка на youtube")
    instagram = models.URLField(blank = True, null=True, verbose_name="Ссылка на instagram")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"

class Contact(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Имя")
    email = models.EmailField(
        verbose_name="Почта"
    )
   
    message = models.CharField(
        max_length=255, 
        verbose_name="Сообщение"
    )
    status_contact = models.BooleanField(
        verbose_name = "Статус контакта",
        default=False
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    def __str__(self):
        return f"{self.name} {self.email}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
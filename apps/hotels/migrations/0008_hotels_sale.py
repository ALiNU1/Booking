# Generated by Django 4.1.3 on 2022-11-18 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0007_remove_hotels_images_hotelimage_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='sale',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

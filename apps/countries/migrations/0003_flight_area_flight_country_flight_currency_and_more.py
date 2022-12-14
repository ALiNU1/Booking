# Generated by Django 4.1.3 on 2022-11-24 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_flight_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='area',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight',
            name='country',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight',
            name='currency',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight',
            name='language',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight',
            name='sovereign_state',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight',
            name='visa',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-19 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cruises', '0002_alter_cruisephoto_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cruises',
            name='place',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cruises',
            name='rate',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
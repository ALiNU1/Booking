# Generated by Django 4.1.3 on 2022-11-15 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cruises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('poster', models.ImageField(upload_to='', verbose_name='cruiese/')),
                ('price', models.BigIntegerField()),
            ],
            options={
                'verbose_name': 'Круиз',
                'verbose_name_plural': 'Круизы',
            },
        ),
        migrations.CreateModel(
            name='CruisePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cruisephoto', to='cruises.cruises')),
            ],
        ),
    ]

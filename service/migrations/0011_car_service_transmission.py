# Generated by Django 4.2.1 on 2023-06-12 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_remove_car_service_pmonthly_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car_service',
            name='transmission',
            field=models.CharField(default='v8', max_length=50, verbose_name='Transmission'),
        ),
    ]

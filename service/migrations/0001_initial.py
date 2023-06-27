# Generated by Django 4.2.1 on 2023-06-07 17:41

import autoslug.fields
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car_Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=60)),
                ('year', models.CharField(max_length=4)),
                ('people_sitting', models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4')], max_length=4)),
                ('gasoline', models.CharField(choices=[('Electric', 'Electric'), ('Gasoline', 'Gasoline'), ('Hybrid', 'Hybrid')], max_length=10)),
                ('petrol', models.CharField(max_length=50)),
                ('automatic', models.CharField(choices=[('Automatic', 'Automatic'), ('NotAutomatic', 'NotAutomatic')], max_length=50)),
                ('price', models.IntegerField(default=0, verbose_name='Your Price Field')),
                ('front_car_image', models.ImageField(upload_to='static/images/featured_cars', verbose_name='Front Page Car Photo')),
                ('car_name_slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='car_name', unique=True)),
                ('car_image_1', models.ImageField(default='No information available', upload_to='static/images/product_pics', verbose_name='Detail CAR Image')),
                ('car_image_2', models.ImageField(default='No information available', upload_to='static/images/product_pics')),
                ('car_image_3', models.ImageField(default='No information available', upload_to='static/images/product_pics')),
                ('car_image_4', models.ImageField(blank=True, upload_to='static/images/product_pics')),
                ('car_image_5', models.ImageField(blank=True, upload_to='static/images/product_pics')),
                ('car_image_6', models.ImageField(blank=True, upload_to='static/images/product_pics')),
                ('car_image_7', models.ImageField(blank=True, upload_to='static/images/product_pics')),
                ('Pfree_delivery', models.CharField(choices=[('Free Delivery', 'Free Delivery'), ('No Free_Delivery', 'No Free_Delivery')], default='Free Delivery', max_length=30, verbose_name='Delivery Type')),
                ('Prating', models.FloatField(verbose_name='Rating')),
                ('About_item', tinymce.models.HTMLField(max_length=640, verbose_name='About Item')),
                ('Pweekly_price', models.IntegerField(default=0, verbose_name='Your weekly price')),
                ('Pmonthly_price', models.IntegerField(default=0, verbose_name='Your monthly price')),
                ('Psecurity_price', models.IntegerField(default=0, verbose_name='Your security price')),
                ('Pallow_km', models.IntegerField(default=0, verbose_name='Your allowed KM')),
                ('Pinsurance', models.CharField(choices=[('Comprehensive', 'Comprehensive'), ('Not Comprehensive', 'Not Comprehensive')], default='Comprehensive', max_length=30, verbose_name='Insurance Type')),
                ('Prental_overview_1', tinymce.models.HTMLField(verbose_name='Rental overview 1')),
                ('Prental_overview_2', tinymce.models.HTMLField(verbose_name='Rental overview 2')),
                ('AirConditioner', models.CharField(choices=[('✅', '✅'), ('❌', '❌')], default='✅', max_length=10)),
                ('CruiseControl', models.CharField(choices=[('✅', '✅'), ('❌', '❌')], default='✅', max_length=10)),
                ('Push_Button_Start', models.CharField(choices=[('✅', '✅'), ('❌', '❌')], default='✅', max_length=10)),
                ('Front_Rear_Airbags', models.CharField(choices=[('✅', '✅'), ('❌', '❌')], default='✅', max_length=10)),
                ('Parking_sensors', models.CharField(choices=[('✅', '✅'), ('❌', '❌')], default='✅', max_length=10)),
                ('Leather_Seats', models.CharField(choices=[('✅', '✅'), ('❌', '❌')], default='✅', max_length=10)),
                ('Steering_Assist', models.CharField(choices=[('✅', '✅'), ('❌', '❌')], default='✅', max_length=10)),
                ('Power_Seats', models.CharField(choices=[('✅', '✅'), ('❌', '❌')], default='✅', max_length=10)),
                ('Brake_Assist', models.CharField(choices=[('✅', '✅'), ('❌', '❌')], default='✅', max_length=10)),
                ('built_in_gps', models.CharField(choices=[('✅', '✅'), ('❌', '❌')], default='✅', max_length=10)),
                ('USB_Charging_Point', models.CharField(choices=[('✅', '✅'), ('❌', '❌')], default='✅', max_length=10)),
                ('Crash_Sensor', models.CharField(choices=[('✅', '✅'), ('❌', '❌')], default='✅', max_length=10)),
                ('Climate_Control', models.CharField(choices=[('✅', '✅'), ('❌', '❌')], default='✅', max_length=10)),
                ('GCC_Specs', models.CharField(choices=[('✅', '✅'), ('❌', '❌')], default='✅', max_length=10)),
                ('delivery_and_pickup', tinymce.models.HTMLField()),
            ],
        ),
    ]
# Generated by Django 4.2.1 on 2023-06-11 13:56

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_car_service_meta_desc_car_service_meta_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_service',
            name='About_item',
            field=tinymce.models.HTMLField(verbose_name='About Item'),
        ),
    ]

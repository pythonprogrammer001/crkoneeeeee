# Generated by Django 4.2.1 on 2023-06-13 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0014_alter_car_service_car_doors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car_service',
            old_name='year',
            new_name='model_year',
        ),
    ]

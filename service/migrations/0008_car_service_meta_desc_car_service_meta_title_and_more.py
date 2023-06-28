# Generated by Django 4.2.1 on 2023-06-11 13:26

from django.db import migrations, models
import service.models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_alter_blog_section_blog_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='car_service',
            name='meta_desc',
            field=models.CharField(blank=True, max_length=600, verbose_name='Meta Desciption'),
        ),
        migrations.AddField(
            model_name='car_service',
            name='meta_title',
            field=models.CharField(blank=True, max_length=500, verbose_name='Meta title'),
        ),
        migrations.AlterField(
            model_name='car_service',
            name='car_image_1',
            field=models.ImageField(default='No information available', upload_to=service.models.get_upload_path_product, verbose_name='Detail CAR Image'),
        ),
        migrations.AlterField(
            model_name='car_service',
            name='car_image_2',
            field=models.ImageField(default='No information available', upload_to=service.models.get_upload_path_product),
        ),
        migrations.AlterField(
            model_name='car_service',
            name='car_image_3',
            field=models.ImageField(default='No information available', upload_to=service.models.get_upload_path_product),
        ),
        migrations.AlterField(
            model_name='car_service',
            name='car_image_4',
            field=models.ImageField(blank=True, upload_to=service.models.get_upload_path_product),
        ),
        migrations.AlterField(
            model_name='car_service',
            name='car_image_5',
            field=models.ImageField(blank=True, upload_to=service.models.get_upload_path_product),
        ),
        migrations.AlterField(
            model_name='car_service',
            name='car_image_6',
            field=models.ImageField(blank=True, upload_to=service.models.get_upload_path_product),
        ),
        migrations.AlterField(
            model_name='car_service',
            name='car_image_7',
            field=models.ImageField(blank=True, upload_to=service.models.get_upload_path_product),
        ),
        migrations.AlterField(
            model_name='car_service',
            name='front_car_image',
            field=models.ImageField(upload_to=service.models.get_upload_path, verbose_name='Front Page Car Photo'),
        ),
    ]

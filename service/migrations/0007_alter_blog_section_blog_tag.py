# Generated by Django 4.2.1 on 2023-06-09 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_blog_section_blog_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_section',
            name='blog_tag',
            field=models.CharField(blank=True, max_length=100, verbose_name='Blog Tag'),
        ),
    ]

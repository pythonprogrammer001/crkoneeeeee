# Generated by Django 4.2.1 on 2023-06-08 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_remove_blog_section_user_comment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_section',
            name='blog_front_pg_img',
        ),
        migrations.AlterField(
            model_name='blog_section',
            name='date_field',
            field=models.DateField(default='June, 08, 2023'),
        ),
    ]
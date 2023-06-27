from django.contrib import admin
from .models import *

# class carservice_models(models.Model):
#     list_display = ('car_name','year','people_sitting','front_car_image','car_image_1','car_image_2','car_image_3','car_image_4','car_image_5','car_image_6','car_image_7','Pfree_delivery'
#                     ,'Pweekly_price','Pmonthly_price','Psecurity_price','Pallow_km','Pinsurance')

admin.site.register(Car_Service)

admin.site.register(blog_section)

# Register your models here.

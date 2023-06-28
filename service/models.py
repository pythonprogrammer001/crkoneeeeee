from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField
from datetime import datetime
import os
from django.utils.text import slugify
from django.core.validators import MaxLengthValidator

##################### front page details
pp_sitting = [
('2', '2'),
('3', '3'),
('4', '4'),
('5', '5'),
('6', '6'),
('7', '7'),
('8', '8'),
]


doors = [
('2', '2'),
('3', '3'),
('4', '4'),
('5', '5'),
]

cbaggage = [
('2', '2'),
('3', '3'),
('4', '4'),
('5', '5'),
]


gaso = [
    ("Electric", "Electric"),
    ("Gasoline", "Gasoline"),
    ("Hybrid", "Hybrid"),
]

autoaa = [
    ("Automatic","Automatic"),
    ("Manual","Manual"),
    ("Automatic or Manual","Automatic or Manual"),
]

#####################










########################################################### product details

free_dev = [
    ("Free Delivery","Free Delivery"),
    ("No Free_Delivery","No Free_Delivery"),
]

insurance = [
    ("Comprehensive","Comprehensive"),
    ("Not Comprehensive","Not Comprehensive"),
]


right_wrong = [
    ("✅","✅"),
    ("❌","❌"),
]








# rating = [
#     ("1.0", "1.0"), ("1.1", "1.1"), ("1.2", "1.2"), ("1.3", "1.3"), ("1.4", "1.4"), 
#     ("1.5", "1.5"), ("1.6", "1.6"), ("1.7", "1.7"), ("1.8", "1.8"), ("1.9", "1.9"), 
#     ("2.0", "2.0"), ("2.1", "2.1"), ("2.2", "2.2"), ("2.3", "2.3"), ("2.4", "2.4"), 
#     ("2.5", "2.5"), ("2.6", "2.6"), ("2.7", "2.7"), ("2.8", "2.8"), ("2.9", "2.9"), 
#     ("3.0", "3.0"), ("3.1", "3.1"), ("3.2", "3.2"), ("3.3", "3.3"), ("3.4", "3.4"), 
#     ("3.5", "3.5"), ("3.6", "3.6"), ("3.7", "3.7"), ("3.8", "3.8"), ("3.9", "3.9"), 
#     ("4.0", "4.0"), ("4.1", "4.1"), ("4.2", "4.2"), ("4.3", "4.3"), ("4.4", "4.4"), 
#     ("4.5", "4.5"), ("4.6", "4.6"), ("4.7", "4.7"), ("4.8", "4.8"), ("4.9", "4.9"), 
#     ("5.0", "5.0")
# ]


############################################################


def get_upload_path(instance, filename):
    # Generate the slug from the instance's field (e.g., title)
    slug = slugify(instance.car_name)
    # Join the slug with the filename to form the final path
    path = os.path.join('featured_cars', slug, filename)
    return path

def get_upload_path_product(instance, filename):
    # Generate the slug from the instance's field (e.g., title)
    slug = slugify(instance.car_name)
    # Join the slug with the filename to form the final path
    path = os.path.join('product_pics', slug, filename)
    return path





class Car_Service(models.Model):
    car_name = models.CharField(max_length=60)
    model_year = models.CharField(max_length=4)
    people_sitting = models.CharField(max_length=4, choices=pp_sitting, verbose_name='People sitting', default='2')
    car_doors = models.CharField(max_length=4, choices=doors, verbose_name='Car doors', default='2')
    Baggage = models.CharField(max_length=4, choices=cbaggage, verbose_name='Baggage', default='2')
    gasoline = models.CharField(max_length=10, choices= gaso)
    Engine_name = models.CharField(max_length=50,verbose_name='Engine Name', default='v8')
    Horse_power = models.IntegerField(verbose_name='Horse Power', default=0)
    top_speed = models.IntegerField(verbose_name='Top Speed', default=0)
    transmission = models.CharField(max_length=50,verbose_name='Transmission', default='ZF 8-speed')
    petrol = models.CharField(max_length=50)
    automatic= models.CharField(max_length=50,choices=autoaa)
    color = models.CharField(max_length=50, verbose_name='Car color',default='Black')
    price=  models.IntegerField(verbose_name='Your Price Field', default=0)
    car_name_slug = AutoSlugField(populate_from='car_name', unique=True, null=True, default=None)
    front_car_image = models.ImageField(upload_to=get_upload_path, verbose_name='Front Page Car Photo')
    # front_car_image = models.ImageField(upload_to="static/images/featured_cars", verbose_name='Front Page Car Photo')
    

    
    # Pcar_name = models.CharField(max_length=60, verbose_name='Car Name')
    Pfree_delivery = models.CharField(max_length=30, choices=free_dev, default="Free Delivery", verbose_name='Delivery Type')
    # Prating = models.IntegerField(choices=rating, default="4.5",verbose_name='Rating')
    Prating = models.FloatField(verbose_name='Rating')
    # Pprice=  models.IntegerField(default=0, verbose_name='Price/Day')
    # About_item = models.CharField(max_length=640,verbose_name='About Item', default='No information available')
    About_item = models.TextField(validators=[MaxLengthValidator(640)],verbose_name='About item')
    # Pweekly_price=  models.IntegerField(verbose_name='Your weekly price', default=0)
    # Pmonthly_price=  models.IntegerField(verbose_name='Your monthly price', default=0)
    Psecurity_price=  models.IntegerField(verbose_name='Your security price', default=0)
    Pallow_km=  models.IntegerField(verbose_name='Your allowed KM', default=0)
    Pinsurance =models.CharField(max_length=30, choices=insurance, default="Comprehensive",verbose_name='Insurance Type')
















# class Product_details(models.Model):
    car_image_1 = models.ImageField(upload_to=get_upload_path_product, default='No information available', verbose_name='Detail CAR Image')
    # car_image_1 = models.ImageField(upload_to="static/images/product_pics", default='No information available', verbose_name='Detail CAR Image')
    car_image_2 = models.ImageField(upload_to=get_upload_path_product, default='No information available')
    car_image_3 = models.ImageField(upload_to=get_upload_path_product, default='No information available')
    car_image_4 = models.ImageField(upload_to=get_upload_path_product, blank=True)
    car_image_5 = models.ImageField(upload_to=get_upload_path_product, blank=True)
    car_image_6 = models.ImageField(upload_to=get_upload_path_product, blank=True)
    car_image_7 = models.ImageField(upload_to=get_upload_path_product, blank=True)
    car_image_8 = models.ImageField(upload_to=get_upload_path_product, blank=True)
    car_image_9 = models.ImageField(upload_to=get_upload_path_product, blank=True)
    car_image_10 = models.ImageField(upload_to=get_upload_path_product, blank=True)
    car_image_11 = models.ImageField(upload_to=get_upload_path_product, blank=True)





    # Prental_overview_1 = models.TextField(verbose_name='Rental overview 1')
    Prental_overview_1 = HTMLField(verbose_name='Rental overview')
    # Prental_overview_2 = models.TextField(verbose_name='Rental overview 2')
    # Prental_overview_2 = HTMLField(verbose_name='Rental overview 2')







    AirConditioner = models.CharField(max_length=10, choices=right_wrong , default="✅")
    CruiseControl = models.CharField(max_length=10, choices=right_wrong, default="✅")
    Push_Button_Start = models.CharField(max_length=10, choices=right_wrong, default="✅")
    Front_Rear_Airbags = models.CharField(max_length=10, choices=right_wrong, default="✅")
    Parking_sensors	 = models.CharField(max_length=10, choices=right_wrong, default="✅")
    Leather_Seats = models.CharField(max_length=10, choices=right_wrong, default="✅")
    Rearview_Camera = models.CharField(max_length=10, choices=right_wrong, default="✅")
    Bluethooth_Audio = models.CharField(max_length=10, choices=right_wrong, default="✅")
    Steering_Assist	 = models.CharField(max_length=10, choices=right_wrong, default="✅")
    Power_Seats	 = models.CharField(max_length=10, choices=right_wrong, default="✅")
    Power_Liftgate	 = models.CharField(max_length=10, choices=right_wrong, default="✅")
    Automatic_Headlights = models.CharField(max_length=10, choices=right_wrong, default="✅")
    Brake_Assist = models.CharField(max_length=10, choices=right_wrong, default="✅")
    Blind_Spot_Assist = models.CharField(max_length=10, choices=right_wrong, default="✅")
    built_in_gps = models.CharField(max_length=10, choices=right_wrong, default="✅")
    USB_Charging_Point = models.CharField(max_length=10, choices=right_wrong, default="✅")
    Crash_Sensor = models.CharField(max_length=10, choices=right_wrong, default="✅")
    Rain_Sensing_Wipers = models.CharField(max_length=10, choices=right_wrong, default="✅")
    Climate_Control	 = models.CharField(max_length=10, choices=right_wrong, default="✅")
    GCC_Specs = models.CharField(max_length=10, choices=right_wrong, default="✅")
    # delivery_and_pickup = models.TextField()
    delivery_and_pickup = HTMLField()
    meta_title = models.CharField(max_length=500, blank=True, verbose_name='Meta title')
    meta_desc = models.CharField(max_length=600, blank=True, verbose_name='Meta Desciption')



    # Pcar_name_slug = AutoSlugField(populate_from='Pcar_name', unique=True, null=True, default=None)

    # people_sitting = models.CharField(max_length=4,choices=years)
    # gasoline = models.CharField(max_length=10, choices= gaso)
    # petrol = models.CharField(max_length=50)
    # automatic= models.CharField(max_length=50,choices=autoaa)
    # car_image = models.ImageField(upload_to="static/images/featured_cars")

    def __str__(self):
        return self.car_name





class blog_section(models.Model):
    front_pg_blog_img = models.ImageField(upload_to="blog_img", verbose_name='Front Page Car Photo')

    # blog_front_pg_img = models.ImageField(upload_to="static/images/blog_img", verbose_name='Blog Page Car Photo')

    title_blog = models.CharField(max_length=100)

    # date_field = models.DateField(default=datetime.now().strftime("%B, %d, %Y"))
    date_field = models.DateField()

    
    blog_tag = models.CharField(max_length=100, blank=True, verbose_name='Blog Tag')

    def save(self, *args, **kwargs):
        if not self.date_field:
            self.date_field = datetime.now().strftime("%B %d, %Y")
        super(blog_section, self).save(*args, **kwargs)


    blog_para = models.CharField(max_length=2000)

    Auth_img = models.ImageField(upload_to="Author_pics", verbose_name='Author Images', default='No information available')

    author_name = models.CharField(max_length=80)

    about_author = models.CharField(max_length=660)

    def __str__(self):
        return self.title_blog





# class Product_detailss(models.Model):



# Create your models here.

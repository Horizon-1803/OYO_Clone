from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class HotelUser(User):
    profile_picture = models.ImageField(upload_to='profile')
    phone_number = models.CharField(max_length=20,unique=True)
    email_token = models.CharField(max_length=100,null=True, blank=False)
    otp = models.CharField(max_length=10,null=True,blank=True)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length = 10 , null = True , blank = True)

class HotelVendor(User):
    profile_picture = models.ImageField(upload_to='profile')
    phone_number = models.CharField(unique=True, max_length=20)
    email_token = models.CharField(max_length=100,null=True, blank=False)
    otp = models.CharField(max_length=10,null=True,blank=True)
    is_verified = models.BooleanField(default=False)

class Amenities(models.Model):
    name = models.CharField(max_length=1000)
    icon = models.ImageField(upload_to="hotels")

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    hotel_slug = models.SlugField(max_length=1000, unique=True)
    hotel_owner = models.ForeignKey(HotelVendor, on_delete=models.CASCADE, related_name="HOTELS")
    amenities = models.ManyToManyField(Amenities)
    price = models.FloatField()
    offer_price = models.FloatField()
    location = models.TextField()
    is_active = models.BooleanField(default=True)

class HotelImages(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="hotel_images")
    image = models.ImageField(upload_to="hotels")

class Hotelmanager(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="hotel_manager")
    manager_name = models.CharField(max_length=100)
    manager_contact = models.CharField(max_length=100)



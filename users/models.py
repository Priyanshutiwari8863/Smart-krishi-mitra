from django.db import models
from django.contrib.auth.models import User


# Farmer Model
class Farmer(models.Model):

    # Link with Django User
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    # Farmer name
    name = models.CharField(max_length=100)

    # Email
    email = models.EmailField()

    # Location
    location = models.CharField(max_length=100, blank=True, null=True)

    # Phone
    phone = models.CharField(max_length=15, blank=True)

    # Soil Type
    soil_type = models.CharField(max_length=50, blank=True)

    # Crop Type
    crop_type = models.CharField(max_length=100, blank=True)

    # Temperature
    temperature = models.IntegerField(default=25)

    # Farm Size
    farm_size = models.CharField(max_length=50, blank=True)

    # Profile Picture
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.name
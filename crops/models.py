from django.db import models

# Create your models here.


# Crop Model
class Crop(models.Model):
    
    # Crop name
    name = models.CharField(max_length=100)

    # Soil type
    soil_type = models.CharField(max_length=100)

    # Season
    season = models.CharField(max_length=100)

    # Water requirement
    water_requirement = models.CharField(max_length=100)
    # Temperature requirement
    temperature = models.IntegerField()

    def __str__(self):
        return self.name
    

class MarketPrice(models.Model):
    crop = models.CharField(max_length=100)
    price = models.IntegerField()
    prediction = models.IntegerField()

    def __str__(self):
        return self.crop    
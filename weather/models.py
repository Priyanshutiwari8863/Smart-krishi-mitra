from django.db import models

class Weather(models.Model):
    location = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    condition = models.CharField(max_length=100)

    def __str__(self):
        return self.location
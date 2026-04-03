from django.db import models


# Disease Model
class Disease(models.Model):

    plant = models.CharField(max_length=100)
    disease_name = models.CharField(max_length=100)
    symptoms = models.TextField()
    solution = models.TextField()

    def __str__(self):
        return self.disease_name


# Medicine Model
class Medicine(models.Model):

    disease = models.ForeignKey(
        Disease,
        on_delete=models.CASCADE,
        related_name='medicines'
    )

    name = models.CharField(max_length=100)
    usage = models.TextField()
    price = models.IntegerField()
    effectiveness = models.IntegerField(default=5)

    def __str__(self):
        return self.name


# Product Model
class Product(models.Model):

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    disease = models.ForeignKey(
        Disease,
        on_delete=models.CASCADE,
        related_name='products',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
    

class Scheme(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.name
    
class Shop(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name    
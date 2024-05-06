from django.contrib.gis.db import models

class Country(models.Model):
    name = models.TextField(max_length=255)
    location = models.PointField()

class City(models.Model):
    name = models.TextField(max_length=255)
    description = models.TextField(max_length=1024)
    photo = models.TextField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    location = models.PointField()

class Capital(models.Model):
    name = models.TextField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    location = models.PointField()
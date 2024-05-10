from django.contrib.gis.db import models

class Country(models.Model):
    name = models.TextField(max_length=255)
    location = models.PointField()

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.TextField(max_length=255)
    description = models.TextField(max_length=1024)
    photo = models.TextField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    location = models.PointField()

    def __str__(self):
        return self.name

class Capital(models.Model):
    name = models.TextField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    location = models.PointField()

    def __str__(self):
        return self.name
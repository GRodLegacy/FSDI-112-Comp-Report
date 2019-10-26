from django.db import models

"""
Possible data types on models:

char (strings)
Int (int)
float (decimal point numbers)
Boolean (true/false)

"""


# Create your models here.
# CRUD
class Genre(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Serie(models.Model):
    class Meta:
        verbose_name_plural = "Series"

    title = models.CharField(max_length = 255)
    season = models.IntegerField()
    episode = models.IntegerField()
    release_year = models.IntegerField()
    in_stock = models.IntegerField()
    price = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    

class Movie(models.Model):
    class Meta:
        verbose_name_plural = "Movies"

    title = models.CharField(max_length = 255)
    release_year = models.IntegerField()
    in_stock = models.IntegerField()
    price = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    director = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
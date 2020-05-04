from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField()
    price = models.FloatField()
    category = models.CharField()

class category(models.Model):
    category = models.ForeignKey(Products.category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
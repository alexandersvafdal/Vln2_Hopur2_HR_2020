from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    image = models.CharField(max_length=999)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.image





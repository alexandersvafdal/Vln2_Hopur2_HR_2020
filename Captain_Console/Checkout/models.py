from django.contrib.auth.models import User
from django.db import models
from user.models import Profile
from django_countries.fields import CountryField

# Create your models here.
class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=10)
    country = models.CharField(max_length=255)
    cart = CountryField(blank_label='Select country')

class Payment(models.Model):
    cardName = models.CharField(max_length=255)
    cardNumber = models.CharField(max_length=16)
    expirationDate = models.CharField(max_length=5)
    CVC = models.CharField(max_length=3)
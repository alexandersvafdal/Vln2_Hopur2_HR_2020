from django.contrib.auth.models import User
from django.db import models
from user.models import Profile
from django_countries.fields import CountryField

# Create your models here.
class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=10)
    country = CountryField(blank_label='Select country')
    cart = models.CharField(max_length=9999999, default="{}")

class Payment(models.Model):
    name_of_cardholder = models.CharField(max_length=255)
    card_number = models.CharField(max_length=16)
    expiration_date = models.CharField(max_length=5)
    CVC = models.CharField(max_length=3)
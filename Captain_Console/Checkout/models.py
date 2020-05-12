from django.contrib.auth.models import User
from django.db import models
from user.models import Profile

# Create your models here.
class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    cart = models.ForeignKey(Profile, on_delete=models.CASCADE)
#ToDo: Save to database - Items ordered and connect to user
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    profile_image = models.CharField(max_length=9999)
    cart = models.CharField(max_length=9999999, blank=True)
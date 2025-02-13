from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SearchQuery(models.Model):
    query = models.CharField(max_length=999)
    date = models.CharField(max_length=999, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

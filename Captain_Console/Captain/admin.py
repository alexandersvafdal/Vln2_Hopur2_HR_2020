from django.contrib import admin
from .models import Products, Category
from user.models import Profile

# Register your models here.

admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Profile)
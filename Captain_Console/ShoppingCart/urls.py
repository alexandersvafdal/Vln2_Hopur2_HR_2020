from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path("addto", views.addToCart, name="add-to-cart"),
]
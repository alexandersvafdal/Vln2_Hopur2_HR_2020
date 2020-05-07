from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.get_product_queryset, name="search-index"),
]
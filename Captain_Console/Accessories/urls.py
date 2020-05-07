from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="accessories-index"),
    re_path(r'(?P<param>.*)', views.manfacturer, name="filter_manufacturer"),
]
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="games-index"),
    re_path(r'(?P<manufacturer>.*)', views.manfacturer, name="filter_manufacturer"),
]
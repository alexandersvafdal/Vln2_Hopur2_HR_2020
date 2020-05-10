from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.shoppingCartData, name="cart-index"),
    path("addto", views.addToCart, name="add-to-cart"),
    path("delete", views.deleteFromCart, name="delete-from-cart")
]
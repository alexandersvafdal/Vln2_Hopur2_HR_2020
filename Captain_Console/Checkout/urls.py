from django.urls import path, re_path
from . import views
from django import forms

from Checkout.forms.checkout_form import ChekcoutForm
from Checkout.preview import OrderPreview

urlpatterns = [
    path('', views.CheckoutView, name="checkout-index"),
    # path('review', views.ReviewView, name="review"),
    re_path(r'^post/$', OrderPreview(ChekcoutForm)),
    path('post/order-success', views.SuccessView, name="order-success"),
]
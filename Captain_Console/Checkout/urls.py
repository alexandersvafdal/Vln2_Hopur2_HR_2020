from django.urls import path
from . import views

urlpatterns = [
    path('', views.CheckoutView, name="checkout-index")
]
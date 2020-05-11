from django.urls import path
from . import views

urlpatterns = [
    path('', views.CheckoutView, name="checkout-index"),
    path('review', views.ReviewView, name="review"),
    path('order-success', views.SuccessView, name="order-success"),

]
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.CheckoutView, name="checkout-index"),
    path('review', views.ReviewView, name="review"),
    path('post/order-success', views.SuccessView, name="order-success"),
]
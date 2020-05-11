from django.urls import path
from . import views

urlpatterns = [
    path('review', views.ReviewView, name="review"),
    path('', views.CheckoutView, name="checkout-index")

]
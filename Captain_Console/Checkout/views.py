from django.shortcuts import render, redirect

# Create your views here.
def CheckoutView(request):
    return render(request, 'payment/checkout.html')

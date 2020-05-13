from django.shortcuts import render, redirect
from Checkout.forms.checkout_form import ChekcoutForm
from user.models import Profile
from .models import Orders
from Captain.models import Products
from django.contrib.auth.decorators import login_required
import json
from formtools.preview import FormPreview

# Create your views here.

@login_required
def CheckoutView(request):
    currentUserId = str(request.user.id)
    user = Profile.objects.get(user_id=currentUserId)
    userCart = json.loads(user.cart)
    products = Products.objects.all().filter(id__in=userCart.keys())

    cart = []
    orderTotal = 0
    for key, value in userCart.items():
        product = products.get(id=key)
        total = float(product.price) * int(value)
        orderTotal += total
        cart.append({"qty": value, "product": product, "total": total})

    context = {'form': ChekcoutForm, 'cartItems': cart, 'orderTotal': orderTotal}

    if request.method == 'POST':
        form = ChekcoutForm(data=request.POST)
        if form.is_valid():
            FormPreview.done(request, form.cleaned_data)
            # cartItems = {'items': cart, 'orderTotal': orderTotal}
            # context = {'paymentInfo': form, 'cart': cartItems}
            # return render(request, 'payment/review.html', context)

    return render(request, 'payment/checkout.html', context)

@login_required()
def ReviewView(request):
    form = ChekcoutForm(data=request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'payment/success.html')

@login_required()
def SuccessView(request):
    return render(request, 'payment/success.html')
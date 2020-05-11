from django.shortcuts import render, redirect
from Checkout.forms.checkout_form import ChekcoutForm
from user.models import Profile
import json
from Captain.models import Products
from django.contrib.auth.decorators import login_required


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
            print("The form is valid")
            return redirect('review')

    return render(request, 'payment/checkout.html', context)

@login_required()
def ReviewView(request):
    if request.method == 'GET':
        form = ChekcoutForm()
    return render(request, 'payment/review.html')

@login_required()
def SuccessView(request):
    return render(request, 'payment/success.html')
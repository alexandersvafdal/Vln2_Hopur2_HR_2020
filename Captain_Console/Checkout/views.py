from django.shortcuts import render, redirect
from Checkout.forms.checkout_form import CheckoutForm, PaymentForm
from django.contrib.auth.models import User
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
    cartDict = {}
    orderTotal = 0
    for key, value in userCart.items():
        product = products.get(id=key)
        total = float(product.price) * int(value)
        orderTotal += total
        cart.append({"qty": value, "product": product, "total": total})
        cartDict[key] = value

    context = {'form': CheckoutForm, 'cartItems': cart, 'orderTotal': orderTotal}

    if request.method == 'POST':
        form = CheckoutForm(data=request.POST)
        if form.is_valid():

            formData = {'paymentInfo': form.cleaned_data}
            request.session['formFilled'] = formData
            request.session['cartOrder'] = cartDict
            return redirect('payment-index')


    return render(request, 'payment/checkout.html', context)


@login_required()
def PaymentView(request):
    formData = request.session.get('formFilled', False)

    if formData != False:
        context = {'form': PaymentForm}

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

        cartItems = {'items': cart, 'orderTotal': orderTotal}

        if request.method == 'POST':
            form = PaymentForm(data=request.POST)
            if form.is_valid():
                cartAllInfo = form.cleaned_data
                name = cartAllInfo['cardName']
                number = cartAllInfo['cardNumber']
                cardInfo = {'cardName': name, 'cardNumber': number[-4:]}
                context = {'paymentInfo': formData['paymentInfo'], 'cardInfo': cardInfo, 'cart': cartItems}
                return render(request, 'payment/review.html', context)
            else:
                context['error'] = form.errors
                return render(request, 'payment/payment.html', context)

        return render(request, 'payment/payment.html', context)

    else:
        print("error redirect")
        return redirect('checkout-index')


@login_required()
def ReviewView(request):
    formData = request.session.get('formFilled', False)
    cartOrder = request.session.get('cartOrder', False)

    if formData and cartOrder:

        if request.method == 'POST':
            user = User.objects.filter(id=request.user.id).first()
            formInfo = formData['paymentInfo']
            form = Orders(
                user=user,
                firstName=formInfo['firstName'],
                lastName=formInfo['lastName'],
                email=formInfo['email'],
                address=formInfo['address'],
                city=formInfo['city'],
                zip=formInfo['zip'],
                country=formInfo['country'],
                cart=cartOrder
                )

            form.save()
            profileUser = Profile.objects.get(user_id=request.user.id)
            profileUser.cart = "{}"
            profileUser.save()
            return redirect('order-success')

        return render(request, 'payment/review.html')

    else:
        return redirect('checkout-index')


@login_required()
def SuccessView(request):
    return render(request, 'payment/success.html')
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from Captain.models import Products
from user.models import Profile

import json

# Create your views here.
@login_required
def addToCart(request):
    if request.method == "POST":
        data = {"status": True}
        body_unicode = request.body.decode('utf-8')
        body = dict((dataString.split("=") for dataString in body_unicode.split("&") if dataString))
        productId = body["productId"]

        if productId and request.user.id:

            user = Profile.objects.get(user_id=request.user.id)
            if user:
                try:
                    cart = json.loads(user.cart)
                except:
                    cart = {}

                if productId in cart:
                    cart[productId] += 1
                else:
                    cart[productId] = 1

                user.cart = json.dumps(cart)
                user.save()
        else:
            data['status'] = False


        return JsonResponse(data)

@login_required
def shoppingCartData(request):
    currentUserId = str(request.user.id)
    user = Profile.objects.get(user_id=currentUserId)
    userCart = json.loads(user.cart)


    products = Products.objects.all().filter(id__in=userCart.keys())

    #qty , SingleProduct
    data = []
    for key, value in userCart.items():
        data.append({"qty": value, "data": products.get(id=key)})
    dictData = {'cartitems': data}

    return render(request, 'shoppingCart/shoppingCartProducts.html', dictData)

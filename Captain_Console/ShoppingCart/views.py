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
        body = dict((toks.split("=") for toks in body_unicode.split("&") if toks))
        productId = body["productId"]
        userId = body["userId"]

        if productId and userId:

            # Er varan til
            user = Profile.objects.get(user_id=userId)
            print(user.name)
            if user:
                if len(user.cart) > 0:
                    user.cart += "," + productId
                else:
                    user.cart += productId
                user.save()

            print(user.cart)

            # Er notandinn til

            # Bæta vorunni við

            pass
        else:
            data['status'] = False


        return JsonResponse(data)
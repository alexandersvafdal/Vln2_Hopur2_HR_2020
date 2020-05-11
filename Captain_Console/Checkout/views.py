from django.shortcuts import render, redirect
from Checout.forms.chechout_form import ChekcoutForm
# Create your views here.
def CheckoutView(request):
    if request.method == 'POST':
        form = ChekcoutForm(data=request.POST)
        if form.is_valid():
            print("The form is valid")
            return redirect('payment/review.html', {
                'form': form
            })
    return render(request, 'payment/checkout.html')

def ReviewView(request):
    if request.method == 'GET':
        form = ChekcoutForm()
    return render(request, 'payment/review.html')

from django.http import HttpResponseRedirect
from user.models import Profile
from formtools.preview import FormPreview
from Checkout.models import Orders

class OrderPreview(FormPreview):
    preview_template = 'payment/review.html'
    form_template = 'payment/checkout.html'


    def done(self, request, cleaned_data):

        # Do something with the cleaned_data, then redirect
        # to a "success" page.
        return HttpResponseRedirect('order-success')
from django import forms
from Checkout.models import Orders, Payment
from django.core.validators import MinLengthValidator, int_list_validator
import datetime
from django_countries.fields import CountryField

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Orders
        exclude = ['id', 'user', 'cart']
        fields = [
            'firstName',
            'lastName',
            'email',
            'address',
            'city',
            'zip',
            'country',
        ]



class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            'cardName',
            'cardNumber',
            'expirationDate',
            'CVC',
        ]


    def clean_expirationDate(self):
        expirationDate = self.cleaned_data['expirationDate']

        try:
            month, year = expirationDate.split('/')
            now = datetime.datetime.now()
            monthNow = now.month
            yearNow = now.year

            if int(month) > 12 or int(month) <= 0:
                raise forms.ValidationError("Invalid date")

            if int(month) < monthNow or int(year) < (yearNow - 2000):
                raise forms.ValidationError("This date has expired")

            return expirationDate

        except ValueError:
            raise forms.ValidationError("Date needs to be in format 'mm/yy'")



    def clean_cardNumber(self):
        cardNumber = self.cleaned_data['cardNumber']

        if len(cardNumber) != 16:
            raise forms.ValidationError("Invalid card number.")
        try:
            number = int(cardNumber)
            return cardNumber
        except ValueError:
            raise forms.ValidationError("Invalid card number.")



    def clean_CVC(self):
        CVC = self.cleaned_data['CVC']

        if len(CVC) != 3:
            raise forms.ValidationError("Invalid CVC.")

        try:
            number = int(CVC)
            return CVC
        except ValueError:
            raise forms.ValidationError("Invalid CVC.")
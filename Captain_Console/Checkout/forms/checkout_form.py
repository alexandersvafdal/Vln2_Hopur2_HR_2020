from django import forms
from django.core.validators import MinLengthValidator, int_list_validator
import datetime
from django_countries.fields import CountryField

class CheckoutForm(forms.Form):
    firstName = forms.CharField()
    lastName = forms.CharField()
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'you@example.com'
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Street 123'
    }))
    city = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'CityName'
    }))
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '111'
    }))
    country = CountryField(blank_label='Select country').formfield()



class PaymentForm(forms.Form):
    cardName = forms.CharField(max_length=255)
    cardNumber = forms.CharField(max_length=16, min_length=16)
    expirationDate = forms.DateField()
    CVC = forms.CharField(max_length=3, min_length=3)

    def clean_date(self):
        expirationDate = self.cleaned_data['expirationDate']
        if expirationDate < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return expirationDate
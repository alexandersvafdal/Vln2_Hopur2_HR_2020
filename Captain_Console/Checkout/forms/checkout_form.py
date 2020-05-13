from django import forms
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


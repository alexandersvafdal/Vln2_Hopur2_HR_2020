from django import forms
from django_countries.fields import CountryField

class ChekcoutForm(forms.Form):
    firstName = forms.CharField()
    lastName = forms.CharField()
    email = forms.CharField()
    addres = forms.CharField()
    country = CountryField(blank_label='Select country')
    zip = forms.CharField()

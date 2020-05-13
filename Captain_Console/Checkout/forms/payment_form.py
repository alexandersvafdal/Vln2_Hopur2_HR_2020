from django import forms
from django.core.validators import MinLengthValidator, int_list_validator
import datetime



class PaymentForm(forms.Form):
    cardName = forms.CharField(max_length=255)
    cardNumber = forms.CharField(verbose_name="Card number", max_length=8,
                                validators=[int_list_validator(sep=''), MinLengthValidator(8), ],
                                default='4444444444444444')
    expirationDate = forms.DateField()
    CVV = forms.CharField(verbose_name="CVV", max_length=3,
                                 validators=[int_list_validator(sep=''), MinLengthValidator(3), ],
                                 default='444')

    def clean_date(self):
        expirationDate = self.cleaned_data['expirationDate']
        if expirationDate < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return expirationDate
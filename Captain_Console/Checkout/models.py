from django.contrib.auth.models import User
from django.db import models
from user.models import Profile

# Create your models here.
class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    cart = models.ForeignKey(Profile, on_delete=models.CASCADE)

class PaymentForm(models.Model):
    cardName = models.CharField(max_length=255)
    cardNumber = models.CharField(verbose_name="Card number", max_length=8,
                                 validators=[int_list_validator(sep=''), MinLengthValidator(8), ],
                                 default='4444444444444444')
    expirationDate = models.DateField()
    CVV = models.CharField(verbose_name="CVV", max_length=3,
                          validators=[int_list_validator(sep=''), MinLengthValidator(3), ],
                          default='444')

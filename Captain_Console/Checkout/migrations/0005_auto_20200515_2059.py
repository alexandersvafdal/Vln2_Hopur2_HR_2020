# Generated by Django 3.0.6 on 2020-05-15 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Checkout', '0004_auto_20200515_1406'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='lastName',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='cardNumber',
            new_name='card_number',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='expirationDate',
            new_name='expiration_date',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='cardName',
            new_name='name_of_cardholder',
        ),
    ]

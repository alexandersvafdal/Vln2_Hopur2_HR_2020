# Generated by Django 2.1.5 on 2020-05-05 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Captain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='manufacturer',
            field=models.CharField(default=True, max_length=255),
            preserve_default=False,
        ),
    ]

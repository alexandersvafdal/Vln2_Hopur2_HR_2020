from django.shortcuts import render
from Captain.models import Products

def index(request):
    allManufacturers = Products.objects.filter(category__name="Games").values_list('manufacturer', flat=True).distinct(
        'manufacturer')


    context = {'products': Products.objects.filter(category__name="Games").order_by('name'),
               'allManufacturers': allManufacturers, 'categoryName': 'games'}

    return render(request, 'category/index.html', context)


def manfacturer(request, manufacturer):
    allManufacturers = Products.objects.filter(category__name="Games").values_list('manufacturer', flat=True).distinct(
        'manufacturer')

    context = {'products': Products.objects.filter(category__name="Games").filter(manufacturer=manufacturer).order_by('name'),
               'allManufacturers': allManufacturers, 'categoryName': 'games'}

    return render(request, 'category/index.html', context)

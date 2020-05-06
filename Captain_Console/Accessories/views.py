from django.shortcuts import render
from Captain.models import Products

# Create your views here.
def index(request):
    allManufacturers = Products.objects.filter(category__name="Accessories").values_list('manufacturer', flat=True).distinct(
        'manufacturer')


    context = {'products': Products.objects.filter(category__name="Accessories").order_by('name'),
               'allManufacturers': allManufacturers, 'categoryName': 'accessories'}

    return render(request, 'category/index.html', context)

def manfacturer(request, manufacturer):
    allManufacturers = Products.objects.filter(category__name="Accessories").values_list('manufacturer', flat=True).distinct(
        'manufacturer')

    context = {'products': Products.objects.filter(category__name="Accessories").filter(manufacturer=manufacturer).order_by('name'),
               'allManufacturers': allManufacturers, 'categoryName': 'accessories'}

    return render(request, 'category/index.html', context)
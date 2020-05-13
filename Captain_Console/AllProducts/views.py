from django.shortcuts import render
from Captain.models import Products

# Create your views here.

def index(request):
    allManufacturers = Products.objects.all().values_list('manufacturer', flat=True).distinct('manufacturer')
    context = {'products':  Products.objects.all().order_by('name'), 'allManufacturers': allManufacturers}

    return render(request, 'category/index.html', context)


def manfacturer(request, param):
    allManufacturers = Products.objects.values_list('manufacturer', flat=True).distinct(
        'manufacturer')




    if param == 'price-ASC':

        context = {
            'products': Products.objects.order_by('price'),
            'allManufacturers': allManufacturers}
        return render(request, 'category/index.html', context)

    elif param == 'price-DESC':

        context = {
            'products': Products.objects.order_by('-price'),
            'allManufacturers': allManufacturers}
        return render(request, 'category/index.html', context)


    elif param == 'name':
        context = {
            'products': Products.objects.order_by('name'),
            'allManufacturers': allManufacturers}
        return render(request, 'category/index.html', context)

    else:
        context = {'products': Products.objects.filter(manufacturer=param).order_by('name'),
               'allManufacturers': allManufacturers}

        return render(request, 'category/index.html', context)

from django.shortcuts import render
from Captain.models import Products

def index(request):
    allManufacturers = Products.objects.filter(category__name="Games").values_list('manufacturer', flat=True).distinct(
        'manufacturer')


    context = {'products': Products.objects.filter(category__name="Games").order_by('name'),
               'allManufacturers': allManufacturers, 'categoryName': 'games'}

    return render(request, 'category/index.html', context)






def manfacturer(request, param):
    allManufacturers = Products.objects.filter(category__name="Games").values_list('manufacturer', flat=True).distinct(
        'manufacturer')

    #splited_manufacturer = manufacturer.split("/")

    #if len(splited_manufacturer) > 1:
    if param == 'price-ASC':

        context = {
            'products': Products.objects.filter(category__name="Games").order_by('price'),
            'allManufacturers': allManufacturers, 'categoryName': 'games'}
        return render(request, 'category/index.html', context)

    elif param == 'price-DESC':

        context = {
            'products': Products.objects.filter(category__name="Games").order_by('-price'),
            'allManufacturers': allManufacturers, 'categoryName': 'games'}
        return render(request, 'category/index.html', context)


    elif param == 'name':
        context = {
            'products': Products.objects.filter(category__name="Games").order_by('name'),
            'allManufacturers': allManufacturers, 'categoryName': 'games'}
        return render(request, 'category/index.html', context)

    else:
        context = {'products': Products.objects.filter(category__name="Games").filter(manufacturer=param).order_by('name'),
               'allManufacturers': allManufacturers, 'categoryName': 'games'}

        return render(request, 'category/index.html', context)


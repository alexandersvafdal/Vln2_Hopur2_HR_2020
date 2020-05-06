from django.shortcuts import render
from Captain.models import Products

# Create your views here.
def index(request):
    allManufacturers = Products.objects.all().filter(category__name="Accessories").values_list('manufacturer',
                                                                                               flat=True)
    context = {'products': Products.objects.filter(category__name="Accessories").order_by('name'),
               'allManufacturers': allManufacturers}
    return render(request, 'category/index.html', context)
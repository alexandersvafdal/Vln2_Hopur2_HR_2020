from django.shortcuts import render
from Captain.models import Products
from django.views import generic

# Create your views here.

def index(request):
    allManufacturers = Products.objects.all().values_list('manufacturer', flat=True).distinct('manufacturer')
    context = {'products':  Products.objects.all().order_by('name'), 'allManufacturers': allManufacturers}

    return render(request, 'captain/index.html', context)

class DetailView(generic.DetailView):
    model = Products
    template_name = 'detailProduct/product.html'

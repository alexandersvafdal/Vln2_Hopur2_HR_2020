from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from Captain.models import Products

# Create your views here.
def get_product_queryset(request, query=None):
    context = {
        'products': Products.objects.filter(name__icontains="Sega Genesis").order_by('name')}

    return render(request, 'searchResult/search_results.html', context)
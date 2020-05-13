from django.shortcuts import render
from Captain.models import Products

# Create your views here.
def index(request):
    context = {'product': Products.objects.filter(category__name="Games").order_by('name')}
    return render(request, 'category/index.html', context)

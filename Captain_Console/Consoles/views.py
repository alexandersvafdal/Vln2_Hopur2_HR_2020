from django.shortcuts import render
from Captain.models import Products

# Create your views here.
def index(request):
    context = {'products': Products.objects.filter(category__name="Consoles").order_by('name')}
    return render(request, 'category/index.html', context)
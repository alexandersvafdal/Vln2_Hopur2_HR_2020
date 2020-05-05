from django.shortcuts import render
from Captain.models import Products
from django.views import generic

# Create your views here.

def index(request):
    context = {'products':  Products.objects.all().order_by('name')}
    return render(request, 'category/index.html', context)

class DetailView(generic.DetailView):
    model = Products
    template_name = 'detailProduct/product.html'

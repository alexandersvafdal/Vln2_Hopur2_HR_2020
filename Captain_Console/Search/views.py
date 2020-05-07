from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from Captain.models import Products

# Create your views here.
def SearchResultsView(request):
    if 'search' in request.GET:
        query = request.GET.get('search')
        productList = Products.objects.filter(name__icontains=query).order_by('name')
        context = {'products': productList, 'query': query}

        return render(request, 'searchResult/search_results.html', context)

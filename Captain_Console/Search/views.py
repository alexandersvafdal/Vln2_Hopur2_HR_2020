from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Captain.models import Products
from Search.models import SearchQuery
from datetime import datetime

# Create your views here.
def SearchResultsView(request):
    if 'search' in request.GET:
        query = request.GET.get('search')
        productList = Products.objects.filter(name__icontains=query).order_by('name')
        context = {'products': productList, 'query': query}

        if request.user.is_authenticated:
            user = User.objects.filter(id=request.user.id).first()
            allQueries = SearchQuery.objects.filter(user=user.id, query=query)

            if (len(allQueries) == 0):
                now = datetime.now()
                now = now.strftime("%d/%m/%Y %H:%M")
                searchText = SearchQuery(query=query, date=now, user=user)
                searchText.save()

        return render(request, 'searchResult/search_results.html', context)

@login_required(login_url="/user/login")
def HistoryView(request):
    user = User.objects.filter(id=request.user.id).first()
    context = {'queries': SearchQuery.objects.filter(user=user.id)}
    return render(request, 'user/search_history.html', context)

@login_required(login_url="/user/login")
def DeleteHistory(request):
    user = User.objects.filter(id=request.user.id).first()
    SearchQuery.objects.filter(user=user.id).delete()
    return render(request, 'user/search_history.html')
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('history', views.HistoryView, name="history-index"),
    path('history/delete', views.DeleteHistory, name="deleteHistory"),
    path('', views.SearchResultsView, name="search-index"),
]
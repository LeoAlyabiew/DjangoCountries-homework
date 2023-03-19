from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('countries-list', views._list),
    path('languages-list', views.languages),
    path('country/<str:country>', views.country_page)
]

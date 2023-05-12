from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home, name='main'),
    path('countries-list/', views.countries_list, name='countries_list'),
    path('languages/', views.languages_list, name='languages_list'),
    path('country/<int:id>', views.country_page, name='country'),
]

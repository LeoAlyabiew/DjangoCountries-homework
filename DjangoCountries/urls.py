from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('countries-list', views._list),
    path('languages-list', views.languages),
    path('country/<int:id>', views.country_page),
    path('converter1', views.convert_countries_to_db),
    path('converter2', views.convert_lang_to_db),
    path('converter3', views.add_lang_to_countries)
]

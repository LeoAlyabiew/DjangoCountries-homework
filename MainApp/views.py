from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from MainApp.models import Country, Language
from django.core.exceptions import ObjectDoesNotExist
import json

with open("country-by-languages.json", "r") as file:
    countries = json.load(file)


def home(request):
    return render(request, 'index.html')


def countries_list(request):
    countries = Country.objects.all()

    context = {
        "countries": countries
    }
    return render(request, 'countries-list.html', context)


def languages_list(request):
    languages = Language.objects.all()

    context = {
        "languages": languages
    }
    return render(request, 'languages-list.html', context)


def country_page(request, id):
    try:
        country = Country.objects.get(id=id)
        # country = get_object_or_404(Country, id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"<h1>Такой страны нет</h1>")
    context = {
        'country': country
    }
    return render(request, 'country-page.html', context)

from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
import json

with open("country-by-languages.json", "r") as file:
    countries = json.load(file)


def home(request):
    return render(request, 'index.html')


def _list(request):
    context = {
        "countries": countries
    }
    return render(request, 'countries_list.html', context)
    # return HttpResponse(countries)


def languages(request):
    languages = []

    for item in countries:
        for i in item["languages"]:
            if i not in languages:
                languages.append(i)
    languages = sorted(languages)

    context = {
        "languages": languages
    }
    return render(request, 'languages-list.html', context)
    # return HttpResponse(countries)


def country_page(request, country):
    for item in countries:
        if item['country'] == country:
            context = {
                'item': item
            }
            return render(request, 'country-page.html', context)

    return HttpResponseNotFound(f"<h1>Такой страны нет ({country})</h1>")

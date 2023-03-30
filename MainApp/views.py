from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from MainApp.models import Country, Language
from django.core.exceptions import ObjectDoesNotExist
import json

with open("country-by-languages.json", "r") as file:
    countries = json.load(file)


def home(request):
    return render(request, 'index.html')


def _list(request):
    countries = Country.objects.all()

    context = {
        "countries": countries
    }
    return render(request, 'countries_list.html', context)
    # return HttpResponse(countries)


def languages(request):
    languages = Language.objects.all()

    context = {
        "languages": languages
    }
    return render(request, 'languages-list.html', context)
    # return HttpResponse(countries)


def country_page(request, id):
    try:
        country = Country.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"<h1>Такой страны нет</h1>")
    context = {
        'country': country
    }
    return render(request, 'country-page.html', context)


def convert_countries_to_db(request):
    for item in countries:
        country = Country(name=item['country'])
        country.save()

    return HttpResponse("Выполнено")


def convert_lang_to_db(request):
    lang = []

    for item in countries:
        for i in item["languages"]:
            if i not in lang:
                lang.append(i)
    lang = sorted(lang)

    for item in lang:
        language = Language(name=item)
        language.save()

    return HttpResponse("Выполнено")


def add_lang_to_countries(request):
    for i, item in enumerate(countries):
        country1 = Country.objects.get(id=i)

        for i, item in enumerate(item["languages"]):
            lang1 = lang1 = Language.objects.get(id=i)
            country1.languages.add(lang1)

    # country1 = Country.objects.get(id=1)
    # country2 = Country.objects.get(id=2)

    # lang1 = Language.objects.get(id=1)
    # lang2 = Language.objects.get(id=2)

    # country1.languages.add(lang1)
    # country2.languages.add(lang1)
    # country2.languages.add(lang2)

    return HttpResponse("Выполнено")

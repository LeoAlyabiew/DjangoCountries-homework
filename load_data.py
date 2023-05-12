import json

from MainApp.models import Country, Language


def save_data_to_db():
    with open("country-by-languages.json", "r") as file:
        countries = json.load(file)

    for country_data in countries:
        country, _ = Country.objects.get_or_create(name=country_data['country'])
        for language_name in country_data['languages']:
            language, _ = Language.objects.get_or_create(name=language_name)
            language.countries_that_use.add(country)


if __name__ == '__main__':
    save_data_to_db()

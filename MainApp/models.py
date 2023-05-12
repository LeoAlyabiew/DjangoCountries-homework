from django.db import models

# Create your models here.


class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Country(models.Model):
    name = models.CharField(max_length=100)
    languages = models.ManyToManyField(to=Language, related_name='countries_that_use')

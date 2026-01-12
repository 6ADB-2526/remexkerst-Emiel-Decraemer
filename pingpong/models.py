from django.db import models

# Create your models here.

class speler(models.Model):
    naam = models.CharField(max_length=25)
    voornaam = models.CharField(max_length=25)
    email = models.EmailField()

class match_punten(models.Model):
    nummerSpeler = models.IntegerField(default=1)
    punten = models.IntegerField(default=0)
    matchCode = models.IntegerField(default=0)
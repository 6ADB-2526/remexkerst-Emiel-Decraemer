from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import speler, match_punten
from django.views.decorators.csrf import csrf_exempt
import json
from django.forms.models import model_to_dict

# Create your views here.
@csrf_exempt
def createUser (request):
    post_data =  json.loads(request.body.decode('utf-8'))

    nieweSpeler = speler()
    nieweSpeler.naam = post_data["naam"]
    nieweSpeler.voornaam = post_data["voornaam"]
    nieweSpeler.email = post_data["email"]

    nieweSpeler.save()
    return HttpResponse("speler toegevoegd")

def oneUser (request, id):
    gevrSpeler = speler.objects.get(pk = id)
    return JsonResponse(model_to_dict(gevrSpeler))

def allUsers (request):
    alleSpelers = speler.objects.all().values()
    return JsonResponse(list(alleSpelers), safe=False)

def matchpoints (request, idSpeler, idMatch):
    gevrSpeler = speler.objects.get(pk = idSpeler)
    gevrMatch = match_punten.objects.all().values(match_punten.punten, id).filter(pk = idMatch)
    dictSpeler = model_to_dict(gevrSpeler)
    dictPunten = model_to_dict(gevrMatch)

    retResultaat = dictSpeler | dictPunten

    return JsonResponse(retResultaat, safe=False)

@csrf_exempt
def createMatch (request):
    post_data =  json.loads(request.body.decode('utf-8'))

    nieuweMatch = match_punten()
    nieuweMatch.nummerSpeler = post_data["nummerSpeler"]
    nieuweMatch.punten = post_data["punten"]
    nieuweMatch.matchCode = post_data["matchCode"]
    nieuweMatch.save()
    return HttpResponse("match aangemaakt")

def totResultaat (request, id):
    totaalPunten = match_punten.objects.all().values(id, match_punten.punten).filter(pk = id)
    for punt in totaalPunten:
        retPunten += totaalPunten.punten
    return JsonResponse(model_to_dict(totaalPunten))

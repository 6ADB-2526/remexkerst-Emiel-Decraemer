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
    return JsonResponse(list(), safe=False)


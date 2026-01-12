from django.urls import path
from . import views

urlpatterns = [
    path("speler/add", views.createUser),
    path("speler/<int:id>", views.oneUser),
    path("speler/", views.allUsers),
    path("matchPunten/resultaat/<int:idSpeler>/<int:idMatch>", views.matchpoints),
    path("createMatch", views.createMatch),
    path("punten/<int:id>", views.totResultaat)
]
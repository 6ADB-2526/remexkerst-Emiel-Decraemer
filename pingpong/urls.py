from django.urls import path
from . import views

urlpatterns = [
    path("speler/add", views.createUser),
    path("speler/<int:id>", views.oneUser),
    path("speler/", views.allUsers),
]
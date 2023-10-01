#Importaciones Django
from django.urls import path

#Importaciones propias
from .views import * #Importa el contenido del módulo views

urlpatterns = [
    path("", inicio, name= "inicio"),
    path("productos/", productos, name= "productos"),
    path("clientes/", clientes, name= "clientes"),
    path("reseñas/", reseñas, name= "reseñas"),
]

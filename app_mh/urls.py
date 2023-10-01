#Importaciones Django
from django.urls import path

#Importaciones propias
from .views import * #Importa el contenido del módulo views

urlpatterns = [
    path("", inicio, name= "inicio"),
    path("productos/", productos, name= "productos"),
    path("clientes/", clientes, name= "clientes"),
    path("reseñas/", reseñas, name= "reseñas"),
    path("productos_form/", productos_form, name= "productos_form"),
    path("productos_busq/", productos_busq, name= "productos_busq"),
    path("productos_rdo/", productos_rdo, name= "productos_rdo"),
    path("clientes_form/", clientes_form, name= "clientes_form"),


    path("reseñas_form/", reseñas_form, name= "reseñas_form"),

    
]

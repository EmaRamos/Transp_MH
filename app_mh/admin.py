#Importaciones Django
from django.contrib import admin

#Importaciones propias
from .models import * #Importa el contenido del módulo models

# Register your models here.

admin.site.register(Productos)

admin.site.register(Clientes)

admin.site.register(Comentarios)
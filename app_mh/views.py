from django.shortcuts import render

# Create your views here.

#Vista de inicio
def inicio(request):
    return render(request, "app_mh/inicio.html")

#Vista de productos
def productos(request):
    return render(request, "app_mh/productos.html")

#Vista de clientes
def clientes(request):
    return render(request, "app_mh/clientes.html")

#Vista de comentarios
def reseñas(request):
    return render(request, "app_mh/reseñas.html")

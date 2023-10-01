#Importaciones Django
from django.shortcuts import render
from django.http import HttpResponse

#Importaciones propias
from .forms import * #Importa el contenido del módulo forms
from .models import * #Importa el contenido del módulo models

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

#Vista de ingreso de productos
def productos_form(request):

    if request.method == "POST": #Verifica si la solicitud HTTP es de tipo POST

        form1= Form_Productos(request.POST) #Crea una instancia del formulario Form_Productos con los datos POST

        if form1.is_valid(): #Verifica si el formulario es válido

            info= form1.cleaned_data #Obtiene los datos validados del formulario

            #Crea una instancia del modelo Productos con los datos del formulario
            producto= Productos(nombre= info["nombre"],
                                largo_cm= info["largo_cm"],
                                ancho_cm= info["ancho_cm"],
                                alto_cm= info["alto_cm"],
                                stock_uni= info["stock_uni"],
                                precio_uni= info["precio_uni"],
                                )
            
            producto.save() #Guarda el producto en la base de datos

            return render(request, "app_mh/inicio.html") #Redirige al vista de inicio
    
    else:

        form1= Form_Productos() #Si la solicitud no es POST entonces crea un formulario vacío

    return render(request, "app_mh/productos_form.html", {"form1": form1}) #Renderiza el template "productos_form.html" y pasa el formulario como contexto

#Vista de búsqueda de productos
def productos_busq(request):


    return render(request, "app_mh/inicio.html")

#Vista de resultados de la búsqueda de productos
def productos_rdo(request):

    if request.GET["nombre"]: #Verifica si se ha proporcionado un valor para el parámetro "nombre" en la solicitud GET

        nombre= request.GET["nombre"]
        
        productos= Productos.objects.filter(nombre__iexact= nombre) #Filtra en la base de datos los productos con el "nombre" coincidente

        return render(request, "app_mh/inicio.html", {"productos": productos}) # Renderiza el template de "inicio.html" y pasa los productos como contexto
    
    else:

        respuesta= "No enviaste datos." #Respuesta en caso de que no se proporcionara un valor para el parámetro "nombre"

    return HttpResponse(respuesta)

#Vista de ingreso de clientes
def clientes_form(request):

    if request.method == "POST": #Verifica si la solicitud HTTP es de tipo POST

        form1= Form_Clientes(request.POST) #Crea una instancia del formulario Form_Clientes con los datos POST

        if form1.is_valid(): #Verifica si el formulario es válido

            info= form1.cleaned_data #Obtiene los datos validados del formulario

            #Crea una instancia del modelo Clientes con los datos del formulario
            cliente= Clientes(nombre= info["nombre"],
                                apellido= info["apellido"],
                                direccion= info["direccion"],
                                telefono= info["telefono"],
                                email= info["email"],
                                )
            
            cliente.save() #Guarda el cliente en la base de datos

            return render(request, "app_mh/inicio.html") #Redirige al vista de inicio
    
    else:

        form1= Form_Clientes() #Si la solicitud no es POST entonces crea un formulario vacío

    return render(request, "app_mh/clientes_form.html", {"form1": form1}) #Renderiza el template "clientes_form.html" y pasa el formulario como contexto

#Vista de ingreso de clientes
def reseñas_form(request):

    if request.method == "POST": #Verifica si la solicitud HTTP es de tipo POST

        form1= Form_Comentarios(request.POST) #Crea una instancia del formulario Form_Comentarios con los datos POST

        if form1.is_valid(): #Verifica si el formulario es válido

            info= form1.cleaned_data #Obtiene los datos validados del formulario

            #Crea una instancia del modelo Comentarios con los datos del formulario
            comentario= Comentarios(nombre= info["nombre"],
                                apellido= info["apellido"],
                                comentario= info["comentario"],
                                )
            
            comentario.save() #Guarda el comentario en la base de datos

            return render(request, "app_mh/inicio.html") #Redirige al vista de inicio
    
    else:

        form1= Form_Comentarios() #Si la solicitud no es POST entonces crea un formulario vacío

    return render(request, "app_mh/reseñas_form.html", {"form1": form1}) #Renderiza el template "reseñas_form.html" y pasa el formulario como contexto

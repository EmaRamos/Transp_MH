#Importaciones Django
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


#Formulario para ingresar productos
class Form_Productos(forms.Form):
    nombre= forms.CharField(max_length= 30) #Indica el nombre del producto
    largo_cm= forms.DecimalField(max_digits= 6, decimal_places= 2, validators=[MinValueValidator(0)]) #Indica el largo (cm) del producto. No admite valores negativos
    ancho_cm= forms.DecimalField(max_digits= 6, decimal_places= 2, validators=[MinValueValidator(0)]) #Indica el ancho (cm) del producto. No admite valores negativos
    alto_cm= forms.DecimalField(max_digits= 6, decimal_places= 2, validators=[MinValueValidator(0)]) #Indica el alto (cm) del producto. No admite valores negativos
    stock_uni= forms.IntegerField(validators=[MinValueValidator(0)]) #Stock en unidades del producto. No admite valores negativos
    precio_uni= forms.DecimalField(max_digits= 10, decimal_places= 2, validators=[MinValueValidator(0)]) #Precio unitario del producto. No admite valores negativos

#Formulario para ingresar clientes
class Form_Clientes(forms.Form):
    nombre= forms.CharField(max_length= 30) #Indica el nombre del cliente
    apellido= forms.CharField(max_length= 30) #Indica el apellido del cliente
    direccion= forms.CharField(max_length= 50) #Indica la dirección del cliente
    telefono= forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999999999)]) #Indica el número de teléfono del cliente. No admite valores negativos
    email= forms.EmailField() #Indica el email del cliente

#Formulario para ingresar comentarios de los clientes
class Form_Comentarios(forms.Form):
    nombre= forms.CharField(max_length= 30) #Indica el nombre del cliente
    apellido= forms.CharField(max_length= 30) #Indica el apellido del cliente
    comentario= forms.CharField(max_length= 255) #Indica el comentario del cliente sobre los productos y el servicio recibido

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

#Productos a la venta en la página
class Productos(models.Model):
    nombre= models.CharField(max_length= 30) #Indica el nombre del producto
    largo_cm= models.DecimalField(max_digits= 6, decimal_places= 2, validators=[MinValueValidator(0)]) #Indica el largo (cm) del producto. No admite valores negativos
    ancho_cm= models.DecimalField(max_digits= 6, decimal_places= 2, validators=[MinValueValidator(0)]) #Indica el ancho (cm) del producto. No admite valores negativos
    alto_cm= models.DecimalField(max_digits= 6, decimal_places= 2, validators=[MinValueValidator(0)]) #Indica el alto (cm) del producto. No admite valores negativos
    stock_uni= models.PositiveIntegerField(validators=[MinValueValidator(0)]) #Stock en unidades del producto. No admite valores negativos
    precio_uni= models.DecimalField(max_digits= 10, decimal_places= 2, validators=[MinValueValidator(0)]) #Precio unitario del producto. No admite valores negativos

#Clientes
class Clientes(models.Model):
    nombre= models.CharField(max_length= 30) #Indica el nombre del cliente
    apellido= models.CharField(max_length= 30) #Indica el apellido del cliente
    direccion= models.CharField(max_length= 50) #Indica la dirección del cliente
    telefono= models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999999999)]) #Indica el número de teléfono del cliente. No admite valores negativos
    email= models.EmailField() #Indica el email del cliente

#Comentarios de los clientes
class Comentarios(models.Model):
    nombre= models.CharField(max_length= 30) #Indica el nombre del cliente
    apellido= models.CharField(max_length= 30) #Indica el apellido del cliente
    comentario= models.CharField(max_length= 255) #Indica el comentario del cliente sobre los productos y el servicio recibido

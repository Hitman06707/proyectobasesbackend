from django.db import models
from client.models import Cliente

# Create your models here.
class Detalle_producto(models.Model):
    id_detalle_producto = models.AutoField   (primary_key=True, unique=True)
    marca               = models.CharField   (max_length=50, verbose_name='Nombre')
    material            = models.CharField   (max_length=50, verbose_name='material')
    talla               = models.CharField   (max_length=50, verbose_name='talla')

class Producto (models.Model):
	CATEGORIA_CHOICES = [(1, 'Mujer'), (2, 'Hombre'), (3, 'Unisex')]
	EXISTENCIA_CHOICES = [(0, 'Disponible'), (1, 'No Disponible')]
	id_producto         = models.AutoField    (primary_key=True, unique=True)
	nombre_producto     = models.CharField    (max_length=100, verbose_name='Nombre Producto')
	detalle_producto    = models.ForeignKey   (Detalle_producto, on_delete=models.CASCADE, verbose_name='Detalle producto')
	categoria           = models.CharField    (choices=CATEGORIA_CHOICES , max_length=50, verbose_name='Categoria') # CHECK( CATEGORIA IN('Mujer','Hombre', 'Unisex') ) ,
	cantidad            = models.IntegerField (verbose_name='Cantidad')
	existencia          = models.CharField    (choices=EXISTENCIA_CHOICES ,max_length=15, verbose_name='Existencia') # CHECK( EXISTENCIA IN('Disponible','No Disponible') ) ,
	precio_venta        = models.IntegerField (verbose_name='precio_venta') 
	precio_compra       = models.IntegerField (verbose_name='precio compra') 
	promocion           = models.IntegerField (verbose_name='promocion') 
	descuento           = models.IntegerField (verbose_name='descuento') 
	
class Vista_producto (models.Model):
    id_vista_producto   = models.AutoField    (primary_key=True, unique=True)
    producto            = models.ForeignKey  (Producto, on_delete=models.CASCADE, verbose_name='Producto')
    cliente             = models.ForeignKey  (Cliente,  on_delete=models.CASCADE, verbose_name='Cliente') 



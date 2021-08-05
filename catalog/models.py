from django.db import models

# Create your models here.
class Detalle_producto(models.Model):
    id_detalle_producto = models.AutoField   (primary_key=True, unique=True)
    marca               = models.CharField   (max_length=50, verbose_name='Nombre')
    material            = models.CharField   (max_length=50, verbose_name='material')
    talla               = models.CharField   (max_length=50, verbose_name='talla')

class Producto (models.Model):
	id_producto         = models.AutoField    (primary_key=True, unique=True)
	nombre_producto     = models.CharField    (max_length=100, verbose_name='Nombre Producto')
	detalle_producto    = models.ForeignKey   (detalle_producto, on_delete=models.CASCADE, verbose_name='detalle producto')
	categoria           = models.CharField    (max_length=50, verbose_name='Nombre') # CHECK( CATEGORIA IN('Mujer','Hombre', 'Unisex') ) ,
	cantidad            = models.IntegerField (verbose_name='Numero Casa')
	existencia          = models.CharField    (max_length=15, verbose_name='Nombre') # CHECK( EXISTENCIA IN('Disponible','No Disponible') ) ,
	precio_venta        = models.IntegerField (verbose_name='precio_venta') 
	precio_compra       = models.IntegerField (verbose_name='precio compra') 
	promocion           = models.IntegerField (verbose_name='promocion') 
	descuento           = models.IntegerField (verbose_name='descuento') 
	
class Vista_producto (models.Model):
    id_vista_producto   models.AutoField    (primary_key=True, unique=True)
    producto            models.ForeignKey  (Producto, on_delete=models.CASCADE, verbose_name='Producto')
    cliente             models.ForeignKey  (Cliente,  on_delete=models.CASCADE, verbose_name='Cliente') 



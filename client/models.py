from django.db import models

# Create your models here.
class Pais(models.Model):
    id_pais          = models.AutoField   (primary_key=True, unique=True)
    codigo_postal    = models.IntegerField(verbose_name='Código Postal')
    nombre           = models.CharField   (max_length=100, verbose_name='Nombre')
    ciudad           = models.CharField   (max_length=100, verbose_name='Ciudad')

class Region(models.Model):
    id_region        = models.AutoField   (primary_key=True, unique=True)
    nombre           = models.CharField   (max_length=100, verbose_name='Nombre')
    pais             = models.ForeignKey  (Pais, on_delete=models.CASCADE, verbose_name='Pais')

class Direccion(models.Model):
	id_direccion     = models.AutoField   (primary_key=True, unique=True)
	region           = models.ForeignKey  (Region, on_delete=models.CASCADE, verbose_name='Region')
	calle            = models.CharField   (max_length=100, verbose_name='Calle')
	avenida          = models.CharField   (max_length=100, verbose_name='Avenida')
	numero_casa      = models.IntegerField(verbose_name='Numero Casa')
	descripcion      = models.CharField   (max_length=100, verbose_name='descripcion')

class Cliente (models.Model):
	id_cliente       = models.AutoField   (primary_key=True, unique=True)
	nombre1          = models.CharField   (max_length=50, verbose_name='Primer nombre')
	nombre2          = models.CharField   (max_length=50, verbose_name='Segundo nombre')
	apellido1        = models.CharField   (max_length=50, verbose_name='Primer apellido')
	apellido2        = models.CharField   (max_length=50, verbose_name='Segundo apellido')
	direccion        = models.ForeignKey  (Direccion, on_delete=models.CASCADE, verbose_name='Direccion') 
	numero_celular   = models.CharField   (max_length= 8, verbose_name='Segundo nombre')
	numero_telefono  = models.CharField   (max_length= 8, verbose_name='Segundo nombre')
	email            = models.CharField   (max_length=50, verbose_name='Segundo nombre')	

	def __str__(self):
		return str(self.nombre1)

class Usuario (models.Model):
    id_login         = models.AutoField   (primary_key=True, unique=True)
    UserName         = models.CharField   (max_length=50, verbose_name='Usuario')
    #Llave            = VARBINARY(8000),
    Llave            = models.CharField   (max_length=50, verbose_name='Llave')
    Nombres          = models.CharField   (max_length=50, verbose_name='Nombres')
    DNI              = models.CharField   (max_length=50, verbose_name='DNI')

from django.db import models
from client.models import Cliente
from catalog.models import Producto

# Create your models here.

class Tipo_Pago(models.Model):
    TIPO_CHOICES = [(1, 'Tarjeta Credito'), (2, 'PAYPAL'), (3, 'Trasferencia Bancaria'), (3, 'Tarjeta Debito')]
    id_detalle_pedido   = models.AutoField   (primary_key=True, unique=True)
    tipo                = models.CharField   (choices=TIPO_CHOICES , max_length=50, verbose_name='Tipo')

class Detalle_pedido(models.Model):
    id_detalle_pedido = models.AutoField   (primary_key=True, unique=True)
    cantidad          = models.IntegerField(verbose_name='Cantidad')
    precio_unitario   = models.IntegerField(verbose_name='Precio Unitario')
    precio_mayoreo    = models.IntegerField(verbose_name='Precio Mayoreo')
    precio_total      = models.IntegerField(verbose_name='Precio Total')

class Pago_pedido(models.Model):
    id_pago_pedido    = models.AutoField   (primary_key=True, unique=True)
    id_tipo_pago      = models.ForeignKey  (Tipo_Pago, on_delete=models.CASCADE, verbose_name='Tipo Pago')

class Pedido(models.Model):
    CATEGORIA_CHOICES = [(1, 'Proceso'), (2, 'Realizado'), (3, 'Cancelado'), (3, 'Fallido')]
    id_pedido          = models.AutoField   (primary_key=True, unique=True)
    codigo_comprobante = models.IntegerField(verbose_name='Codigo Comprobante')
    cliente            = models.ForeignKey  (Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    detalle_pedido     = models.ForeignKey  (Detalle_pedido, on_delete=models.CASCADE, verbose_name='Detalle pedido')           
    producto           = models.ForeignKey  (Producto, on_delete=models.CASCADE, verbose_name='Producto')
    fecha              = models.DateTimeField(verbose_name='Fecha', auto_now_add=True, null=True)
    estado_pedido      = models.CharField   (choices=CATEGORIA_CHOICES ,max_length=50, verbose_name='Estado Pedido')  #CHECK ( ESTADO_PEDIDO IN('Proceso', 'Realizado', 'Cancelado', 'Fallido')            
    pago_pedido        = models.ForeignKey         

class Tipo_entrega_envio(models.Model):
    ENTREGA_CHOICES = [(1, 'Aereo'), (2, 'Terrestre'), (3, 'Maritimo')]
    id_tipo_entrega     = models.AutoField   (primary_key=True, unique=True)
    tipo_entrega        = models.CharField   (choices=ENTREGA_CHOICES ,max_length=50, verbose_name='Estado Pedido')  # 'Areo', 'Terrestre', 'Maritimo'

class Reembolso(models.Model):
    id_reembolso        = models.AutoField   (primary_key=True, unique=True)
    detalle             = models.CharField   (max_length=200, verbose_name='Detalle') 

class Envio(models.Model):
    id_envio            = models.AutoField   (primary_key=True, unique=True)
    pedido              = models.ForeignKey  (Pedido, on_delete=models.CASCADE, verbose_name='Pedido')
    tipo_entrega        = models.ForeignKey  (Tipo_entrega_envio, on_delete=models.CASCADE, verbose_name='Tipo entrega')
    reembolso           = models.ForeignKey  (Reembolso, on_delete=models.CASCADE, verbose_name='Reembolso')
    fecha_envio         = models.DateTimeField(verbose_name='Fecha Envio', auto_now_add=True, null=True)



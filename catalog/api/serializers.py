from rest_framework import serializers
from catalog.models import Detalle_producto, Producto, Vista_producto

class Detalle_productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle_producto
        fields = ["id_detalle_producto","marca","material","talla"]

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ["id_producto","nombre_producto","detalle_producto","categoria","cantidad","existencia","precio_venta","precio_compra","promocion","descuento"]

class Vista_productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vista_producto
        fields = ["id_vista_producto","producto","cliente"]


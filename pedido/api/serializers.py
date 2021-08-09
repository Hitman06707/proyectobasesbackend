from rest_framework import serializers
from pedido.models import Tipo_Pago, Detalle_pedido, Pago_pedido, Pedido, Tipo_entrega_envio, Reembolso, Envio

class Tipo_PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Pago
        fields = ["id_detalle_pedido","tipo"]

class Detalle_pedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle_pedido
        fields = ["id_detalle_pedido","cantidad","precio_unitario","precio_mayoreo","precio_total"]

class Pago_pedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago_pedido
        fields = ["id_pago_pedido","id_tipo_pago"]

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ["id_pedido","codigo_comprobante","cliente","detalle_pedido","producto","fecha","estado_pedido","pago_pedido"] 

class Tipo_entrega_envioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_entrega_envio
        fields = ["id_tipo_entrega","tipo_entrega"] 

class ReembolsoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reembolso
        fields = ["id_reembolso","detalle"] 

class EnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envio
        fields = ["id_envio","pedido","tipo_entrega","reembolso","fecha_envio"] 

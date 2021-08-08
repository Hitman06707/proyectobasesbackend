from django.contrib import admin
from pedido.models import Tipo_Pago,Detalle_pedido,Pago_pedido,Pedido,Tipo_entrega_envio,Reembolso,Envio

# Register your models here.
class Tipo_pagoAdmin(admin.ModelAdmin):
    list_display = ('id_detalle_pedido', 'tipo')

class Detalle_pedidoAdmin(admin.ModelAdmin):
    list_display = ('id_detalle_pedido', 'cantidad', 'precio_unitario', 'precio_mayoreo', 'precio_total')

class Pago_pedidoAdmin(admin.ModelAdmin):
    list_display = ('id_pago_pedido', 'id_tipo_pago')

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id_pedido', 'codigo_comprobante', 'cliente', 'detalle_pedido', 'producto', 'fecha', 'estado_pedido', 'pago_pedido')

class Tipo_entrega_envioAdmin(admin.ModelAdmin):
    list_display = ('id_tipo_entrega', 'tipo_entrega')

class ReembolsoAdmin(admin.ModelAdmin):
    list_display = ('id_reembolso', 'detalle')

class EnvioAdmin(admin.ModelAdmin):
    list_display = ('id_envio', 'pedido' , 'tipo_entrega' , 'reembolso' , 'fecha_envio') 

admin.site.register(Tipo_Pago           , Tipo_pagoAdmin)
admin.site.register(Detalle_pedido      , Detalle_pedidoAdmin)
admin.site.register(Pago_pedido         , Pago_pedidoAdmin)
admin.site.register(Pedido              , PedidoAdmin)
admin.site.register(Tipo_entrega_envio  , Tipo_entrega_envioAdmin)
admin.site.register(Reembolso           , ReembolsoAdmin)
admin.site.register(Envio               , EnvioAdmin)

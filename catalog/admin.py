from django.contrib import admin
from catalog.models import Detalle_producto, Producto, Vista_producto

# Register your models here.
class Detalle_productoAdmin(admin.ModelAdmin):
    list_display = ('id_detalle_producto', 'marca', 'material', 'talla')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre_producto', 'detalle_producto', 'categoria', 'cantidad', 'existencia', 'precio_venta', 'precio_compra', 'promocion', 'descuento' )

class Vista_productoAdmin(admin.ModelAdmin):
    list_display = ('id_vista_producto', 'producto', 'cliente' )

admin.site.register(Detalle_producto, Detalle_productoAdmin)
admin.site.register(Producto        , ProductoAdmin)
admin.site.register(Vista_producto  , Vista_productoAdmin)

from django.contrib import admin
from client.models import Pais, Region, Direccion, Cliente, Usuario

# Register your models here.
class PaisAdmin(admin.ModelAdmin):
    list_display = ('id_pais', 'codigo_postal', 'nombre', 'ciudad')

class RegionAdmin(admin.ModelAdmin):
    list_display = ('id_region', 'nombre', 'pais')

class DireccionAdmin(admin.ModelAdmin):
    list_display = ('id_direccion', 'region', 'calle', 'avenida', 'numero_casa', 'descripcion' )

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre1', 'nombre2', 'apellido1', 'apellido2', 'direccion' , 'numero_celular' , 'numero_telefono' , 'email' )

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_login', 'UserName', 'Llave', 'Nombres', 'DNI' )

admin.site.register(Pais     , PaisAdmin)
admin.site.register(Region   , RegionAdmin)
admin.site.register(Direccion, DireccionAdmin)
admin.site.register(Cliente  , ClienteAdmin)
admin.site.register(Usuario  , UsuarioAdmin)
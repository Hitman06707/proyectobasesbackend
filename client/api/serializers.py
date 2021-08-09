from rest_framework import serializers
from client.models import Pais, Region, Direccion, Cliente, Usuario

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ["id_pais","codigo_postal","nombre","ciudad"]

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["id_region","nombre","pais"]

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ["id_direccion","region","calle","avenida","numero_casa","descripcion"]

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["id_cliente","nombre1","nombre2","apellido1","apellido2","direccion","numero_celular","numero_telefono","email"] 

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["id_login","UserName","Llave","Nombres","DNI"] 

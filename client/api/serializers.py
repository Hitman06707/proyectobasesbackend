from rest_framework import serializers
from client.models import Pais

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ["id_pais","codigo_postal","nombre","ciudad"]

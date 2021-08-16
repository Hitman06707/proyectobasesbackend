from django.core import serializers
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import permission_classes

from client.models  import Pais, Region, Direccion, Cliente, Usuario
#from pedido.models  import Pais, Region, Direccion, Cliente, Usuario
#from catalog.models import Pais, Region, Direccion, Cliente, Usuario

from django.db.models import Count

#from .serializers import PaisSerializer, RegionSerializer, DireccionSerializer, ClienteSerializer, UsuarioSerializer

@permission_classes([])
class usuariospaisesApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        result = Pais.objects.annotate( ccount = Count('region__direccion__cliente' ) )
        #qs_json = serializers.serialize('json', result)
        breakpoint()

        dictionaries = [ obj.as_dict() for obj in result ]
        return Response(json.dumps(dictionaries), status=status.HTTP_200_OK)

        #return Response(qs_json, status=status.HTTP_200_OK )
#        return Response(serializer.data, status=status.HTTP_200_OK)
        

    # 2. Create
    # def post(self, request, *args, **kwargs):
    #     '''
    #     Create the Todo with given todo data
    #     '''
    #     data = {
    #         'task': request.data.get('task'), 
    #         'completed': request.data.get('completed'), 
    #         'user': request.user.id
    #     }
    #     serializer = TodoSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
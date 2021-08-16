# todo/api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from client.models import Pais, Region, Direccion, Cliente, Usuario
from .serializers import PaisSerializer, RegionSerializer, DireccionSerializer, ClienteSerializer, UsuarioSerializer

@permission_classes([])
class PaisListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        paises = Pais.objects.all() # .filter(user = request.user.id)
        serializer = PaisSerializer(paises, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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

@permission_classes([])
class RegionListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        regiones = Region.objects.all() # .filter(user = request.user.id)
        serializer = PaisSerializer(regiones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@permission_classes([])
class DireccionListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        direcciones = Direccion.objects.all() # .filter(user = request.user.id)
        serializer = DireccionSerializer(direcciones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@permission_classes([])
class ClienteListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        clientes = Cliente.objects.all() # .filter(user = request.user.id)
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@permission_classes([])
class UsuarioListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        usuarios = Usuario.objects.all() # .filter(user = request.user.id)
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

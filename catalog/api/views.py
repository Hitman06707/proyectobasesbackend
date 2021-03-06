# todo/api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from catalog.models import Detalle_producto, Producto, Vista_producto
from .serializers import Detalle_productoSerializer, ProductoSerializer, Vista_productoSerializer

@permission_classes([])
class Detalle_productoListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        detalles = Detalle_producto.objects.all() # .filter(user = request.user.id)
        serializer = Detalle_productoSerializer(detalles, many=True)
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
class ProductoListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        productos = Producto.objects.all() # .filter(user = request.user.id)
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@permission_classes([])
class Vista_productoListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        vistas_producto = Vista_producto.objects.all() # .filter(user = request.user.id)
        serializer = Vista_productoSerializer(vistas_producto, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

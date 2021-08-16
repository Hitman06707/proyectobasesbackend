# todo/api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from pedido.models import Tipo_Pago, Detalle_pedido, Pago_pedido, Pedido, Tipo_entrega_envio, Reembolso, Envio
from .serializers import Tipo_PagoSerializer, Detalle_pedidoSerializer, Pago_pedidoSerializer, PedidoSerializer, Tipo_entrega_envioSerializer, ReembolsoSerializer, EnvioSerializer

@permission_classes([])
class Tipo_PagoListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        tipopagos = Tipo_Pago.objects.all() # .filter(user = request.user.id)
        serializer = Tipo_PagoSerializer(tipopagos, many=True)
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
class Detalle_pedidoListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        detalles = Detalle_pedido.objects.all() # .filter(user = request.user.id)
        serializer = Detalle_pedidoSerializer(detalles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@permission_classes([])
class Pago_pedidoListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        pagos = Pago_pedido.objects.all() # .filter(user = request.user.id)
        serializer = Pago_pedidoSerializer(pagos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@permission_classes([])
class PedidoListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        pedidos = Pedido.objects.all() # .filter(user = request.user.id)
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@permission_classes([])
class Tipo_entrega_envioListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        tipoentregas = Tipo_entrega_envio.objects.all() # .filter(user = request.user.id)
        serializer = Tipo_entrega_envioSerializer(tipoentregas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@permission_classes([])
class ReembolsoListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        reembolsos = Reembolso.objects.all() # .filter(user = request.user.id)
        serializer = ReembolsoSerializer(reembolsos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@permission_classes([])
class EnvioListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        envios = Envio.objects.all() # .filter(user = request.user.id)
        serializer = EnvioSerializer(envios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

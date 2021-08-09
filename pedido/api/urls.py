from django.conf.urls import url
from django.urls import path, include
from .views import Tipo_PagoListApiView, Detalle_pedidoListApiView, Pago_pedidoListApiView, PedidoListApiView, Tipo_entrega_envioListApiView, ReembolsoListApiView, EnvioListApiView


urlpatterns = [
    path('tipo_pago', Tipo_PagoListApiView.as_view()),
    path('detalle_pedido', Detalle_pedidoListApiView.as_view()),
    path('pago_pedido', Pago_pedidoListApiView.as_view()),
    path('pedido', PedidoListApiView.as_view()),
    path('tipo_entrega_envio', Tipo_entrega_envioListApiView.as_view()),
    path('reembolso', ReembolsoListApiView.as_view()),
    path('envio', EnvioListApiView.as_view()),
]
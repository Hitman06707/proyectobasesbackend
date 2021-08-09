from django.conf.urls import url
from django.urls import path, include
from .views import Detalle_productoListApiView, ProductoListApiView, Vista_productoListApiView

urlpatterns = [
    path('detalle_producto', Detalle_productoListApiView.as_view()),
    path('producto', ProductoListApiView.as_view()),
    path('vista_producto', Vista_productoListApiView.as_view()),
]
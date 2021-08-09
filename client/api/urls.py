from django.conf.urls import url
from django.urls import path, include
from .views import PaisListApiView, RegionListApiView, DireccionListApiView, ClienteListApiView, UsuarioListApiView


urlpatterns = [
    path('pais', PaisListApiView.as_view()),
    path('region', RegionListApiView.as_view()),
    path('direccion', DireccionListApiView.as_view()),
    path('cliente', ClienteListApiView.as_view()),
    path('usuario', UsuarioListApiView.as_view()),
]
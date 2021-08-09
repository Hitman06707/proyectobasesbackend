from django.conf.urls import url
from django.urls import path, include
from .views import PaisListApiView, RegionListApiView, DireccionListApiView, ClienteListApiView, UsuarioListApiView


urlpatterns = [
    path('Pais', PaisListApiView.as_view()),
    path('Region', RegionListApiView.as_view()),
    path('Direccion', DireccionListApiView.as_view()),
    path('Cliente', ClienteListApiView.as_view()),
    path('Usuario', UsuarioListApiView.as_view()),
]
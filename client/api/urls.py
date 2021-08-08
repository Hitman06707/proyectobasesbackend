from django.conf.urls import url
from django.urls import path, include
from .views import (
    PaisListApiView,
)

urlpatterns = [
    path('', PaisListApiView.as_view()),
]
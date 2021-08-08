
from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    path('api/', include('client.api.urls')),
]
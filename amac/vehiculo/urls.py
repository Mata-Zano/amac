"""
URL configuration for amac project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import *

urlpatterns = [
    path('registro/', registro_vehiculo, name='registro_vehiculo'),
    path('lista/', lista_vehiculos, name='vehiculo_lista'),
    path('addMarca/', addMarca , name='addMarca'),
    path('addModelo/', addModelo , name='addModelo'),
    # path('editarProducto/<int:id>',editProduct, name="editProduct"),
    path('eliminarVehiculo/<int:id>',deleteVehiculo, name="deleteVehiculo"),

]

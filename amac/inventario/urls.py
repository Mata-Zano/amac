from django.urls import path
from inventario.views import *



urlpatterns = [
    path('productos/',productos, name="productos"),
    path('agregarTipo/',addTipo, name="addTipo"),
    path('agregarProducto/',agregarProducto, name="addProduct"),

    # path('editarUsuario/<int:id>',editUser, name="editUser"),
    # path('eliminarUsuario/<int:id>',deleteUser, name="editUser"),


]
from django.urls import path
from inventario.views import *



urlpatterns = [
    path('productos/',productos, name="productos"),
    path('agregarTipo/',addTipo, name="addTipo"),
    path('agregarProducto/',agregarProducto, name="addProduct"), 
    path('editarProducto/<int:id>',editProduct, name="editProduct"),
    path('eliminarProducto/<int:id>',deleteProduct, name="deleteProduct"),

]
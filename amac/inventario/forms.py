from django import forms
from inventario.models import *


class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = ['nombre', 'descripcion']


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['tipo', 'nombre', 'descripcion','imagen'] 


class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['stock', 'fechaIngreso', 'fechaVencimiento', 'stockMinimo']
        
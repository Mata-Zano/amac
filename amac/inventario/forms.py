from django import forms
from inventario.models import Producto, Inventario, Tipo, Proveedor
from django.core.exceptions import ValidationError

class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'agregarproducto-input-text'}),
            'descripcion': forms.Textarea(attrs={'class': 'agregarproducto-textarea', 'rows': 3}),
        }
        labels = {
            'nombre': 'Nombre del Tipo',
            'descripcion': 'Descripción del Tipo',
        }

class ProductoForm(forms.ModelForm):
    tipo = forms.ModelChoiceField(
        queryset=Tipo.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'agregarproducto-select'}),
        label="Tipo de Producto"
    )

    proveedor = forms.ModelChoiceField(
        queryset=Proveedor.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'agregarproducto-select'}),
        label="Proveedor"
    )

    UNIDADES_MEDIDA = [
        ('unidad', 'Unidad'),
        ('galon', 'Galón'),
        ('litro', 'Litro'),
        ('kg', 'Kilogramo'),
    ]

    unidadMedida = forms.ChoiceField(
        choices=UNIDADES_MEDIDA,
        widget=forms.Select(attrs={'class': 'agregarproducto-select'}),
        label="Unidad de Medida",
    )

    class Meta:
        model = Producto
        fields = ['tipo', 'nombre', 'descripcion', 'marca', 'modeloCompatible', 'unidadMedida', 'imagen', 'proveedor']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'agregarproducto-input-text'}),
            'descripcion': forms.Textarea(attrs={'class': 'agregarproducto-textarea', 'rows': 3}),
            'marca': forms.TextInput(attrs={'class': 'agregarproducto-input-text'}),
            'modeloCompatible': forms.CheckboxSelectMultiple(attrs={'class': 'agregarproducto-checkbox-group'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'agregarproducto-input-file'}),
        }
        labels = {
            'nombre': 'Nombre del Producto',
            'descripcion': 'Descripción',
            'marca': 'Marca',
            'imagen': 'Imagen del Producto',
        }
        help_texts = {
            'nombre': 'Introduzca el nombre del producto.',
            'descripcion': 'Proporcione una breve descripción del producto.',
            'marca': 'Especifique la marca del producto si aplica.',
        }

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['fechaVencimiento', 'stock', 'stockMinimo', 'ubicacion']
        widgets = {
            'fechaVencimiento': forms.DateInput(attrs={'class': 'agregarproducto-input-date', 'type': 'date'}),
            'stock': forms.NumberInput(attrs={'class': 'agregarproducto-input-number'}),
            'stockMinimo': forms.NumberInput(attrs={'class': 'agregarproducto-input-number'}),
            'ubicacion': forms.TextInput(attrs={'class': 'agregarproducto-input-text'}),
        }
        labels = {
            'producto': 'Producto',
            'fechaVencimiento': 'Fecha de Vencimiento',
            'stock': 'Stock Actual',
            'stockMinimo': 'Stock Mínimo',
            'ubicacion': 'Ubicación del Producto',
        }
        help_texts = {
            'fechaVencimiento': 'Seleccione la fecha de vencimiento del producto si aplica.',
            'stock': 'Ingrese la cantidad actual en inventario.',
            'stockMinimo': 'Ingrese la cantidad mínima que debe mantenerse en inventario.',
            'ubicacion': 'Indique la ubicación donde se almacena el producto.',
        }

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is not None and stock < 0:
            raise ValidationError('El stock no puede ser negativo.')
        return stock

    def clean_stockMinimo(self):
        stockMinimo = self.cleaned_data.get('stockMinimo')
        if stockMinimo is not None and stockMinimo < 0:
            raise ValidationError('El stock mínimo no puede ser negativo.')
        return stockMinimo
from django import forms
from .models import *
from vehiculo.models import *

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = [ 'color', 'descripcion', 'anio_fabricacion', 'kilometraje', 'patente', 'num_chasis', 'num_motor', 'estado', ]

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre','pais_origen']

class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ['nombre', 'tipo','version','motor' ]

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'precio', 'duracion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'servicio-input-text'}),
            'precio': forms.NumberInput(attrs={'class': 'servicio-input-number'}),
        }
        labels = {
            'nombre': 'Nombre del Servicio',
            'precio': 'Precio del Servicio',
            'duracion': 'Duración Estimada',
        }

class MantencionForm(forms.ModelForm):
    class Meta:
        model = Mantencion
        fields = [ 'revision_inicial', 'servicio', 'precio_total', 'estado', ]
        widgets = {
            'vehiculo': forms.Select(attrs={'class': 'mantencion-select'}),
            'revision_inicial': forms.Textarea(attrs={'class': 'mantencion-textarea'}),
            'servicio': forms.SelectMultiple(attrs={'class': 'mantencion-select-multiple'}),
          
        }
        labels = {
            'vehiculo': 'Vehículo',
            'revision_inicial': 'Revisión Inicial',
            'servicio': 'Servicios',
            'precio_total': 'Precio Total',
            'estado': 'Estado de la Mantención',

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['servicio'].queryset = Servicio.objects.all()
        

class ProductoEnMantencionForm(forms.ModelForm):
    class Meta:
        model = ProductoEnMantencion
        fields = ['producto', 'cantidad', 'precio_total']
        widgets = {
            'precio_total': forms.NumberInput(attrs={'readonly': True}),  # Calculado automáticamente
        }
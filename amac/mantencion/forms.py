from django import forms
from .models import *
from vehiculo.models import *

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = [ 'color', 'descripcion', 'anio_fabricacion', 'kilometraje', 'patente', 'num_chasis', 'num_motor', 'estado', ]
        labels = {
            'descripcion': 'Observacion del vehiculo',
            'descripcion': 'Observacion del vehiculo',
            'anio_fabricacion': 'Año de fabricacion', 
            'estado': 'Estado del vehiculo',


        }
        widgets = {
            'estado': forms.Select(attrs={'class': 'mantencion-select','placeholder': 'Selecciona un estado'}),
            'anio_fabricacion': forms.NumberInput(attrs={'class': 'mantencion-input-number','placeholder': 'Año de fabricación'}),
            'kilometraje': forms.NumberInput(attrs={'class': 'mantencion-input-number','placeholder': 'Ejemplo: 1000Km'}),
            'patente': forms.TextInput(attrs={'class': 'mantencion-input-text','placeholder': 'Ejemplo: GKBB10'}),
            'num_chasis': forms.TextInput(attrs={'class': 'mantencion-input-text','placeholder': 'N° de 17 dígitos'}),
            'num_motor': forms.TextInput(attrs={'class': 'mantencion-input-text','placeholder': 'N° de 14 dígitos'}),
            'descripcion': forms.Textarea(attrs={'class': 'mantencion-textarea','placeholder': 'Observaciones'}),


        }
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre','pais_origen']
        labbels = {
            'nombre': 'Nombre de la marca',
            'pais_origen': 'País de origen',    
            }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'mantencion-input-text','placeholder': 'Ejemplo : Toyota'}),
            'pais_origen': forms.Select(attrs={'class': 'mantencion-select','placeholder': 'Selecciona un país'}),}

class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ['nombre', 'tipo','version','motor' ]
        labels = {
            'nombre': 'Nombre del modelo',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'mantencion-input-text','placeholder': 'Ejemplo : Corolla'}),
            'tipo': forms.Select(attrs={'class': 'mantencion-select','placeholder': 'Selecciona un tipo'}),
            'version': forms.TextInput(attrs={'class': 'mantencion-input-text','placeholder': 'Ejemplo : 2022'}),
            'motor': forms.TextInput(attrs={'class': 'mantencion-input-text','placeholder': 'Ejemplo : 1.2'}),}

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
        fields = [ 'recepcionista','revision_inicial', 'servicio' , 'estado', 'precio_total',]
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
        widgets = {
            'recepcionista': forms.Select(attrs={'class': 'mantencion-select'}), 
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['servicio'].queryset = Servicio.objects.all()
        

class ProductoEnMantencionForm(forms.ModelForm):
    class Meta:
        model = ProductoEnMantencion
        fields = ['producto', 'cantidad', 'precio_total']

from django import forms
from .models import Vehiculo, Marca, Modelo
from django.core.exceptions import ValidationError

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre', 'pais_origen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'marca-input-text'}),
            'pais_origen': forms.TextInput(attrs={'class': 'marca-input-text'}),
        }
        labels = {
            'nombre': 'Nombre de la Marca',
            'pais_origen': 'País de Origen',
        }

class ModeloForm(forms.ModelForm):
    marca = forms.ModelChoiceField(
        queryset=Marca.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'modelo-select'}),
        label="Marca"
    )

    class Meta:
        model = Modelo
        fields = ['marca', 'nombre', 'tipo', 'version', 'motor']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'modelo-input-text'}),
            'tipo': forms.TextInput(attrs={'class': 'modelo-input-text'}),
            'version': forms.TextInput(attrs={'class': 'modelo-input-text'}),
            'motor': forms.TextInput(attrs={'class': 'modelo-input-text'}),
        }
        labels = {
            'nombre': 'Nombre del Modelo',
            'tipo': 'Tipo del Modelo',
            'version': 'Versión del Modelo',
            'motor': 'Motor del Modelo',
        }
        help_texts = {
            'nombre': 'Introduzca el nombre del modelo.',
            'tipo': 'Indique el tipo del modelo.',
            'version': 'Especifique la versión del modelo.',
            'motor': 'Proporcione el tipo de motor del modelo.',
        }

class VehiculoForm(forms.ModelForm):
    marca = forms.ModelChoiceField(
        queryset=Marca.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'vehiculo-select'}),
        label="Marca"
    )
    modelo = forms.ModelChoiceField(
        queryset=Modelo.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'vehiculo-select'}),
        label="Modelo"
    )

    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'descripcion', 'anio_fabricacion', 'color', 'patente', 'num_chasis', 'num_motor', 'estado', 'kilometraje']
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'vehiculo-input-text'}),
            'anio_fabricacion': forms.NumberInput(attrs={'class': 'vehiculo-input-number'}),
            'color': forms.TextInput(attrs={'class': 'vehiculo-input-text'}),
            'patente': forms.TextInput(attrs={'class': 'vehiculo-input-text'}),
            'num_chasis': forms.TextInput(attrs={'class': 'vehiculo-input-text'}),
            'num_motor': forms.TextInput(attrs={'class': 'vehiculo-input-text'}),
            'estado': forms.TextInput(attrs={'class': 'vehiculo-input-text'}),
            'kilometraje': forms.TextInput(attrs={'class': 'vehiculo-input-text'}),
        }
        labels = {
            'descripcion': 'Descripción del Vehículo',
            'anio_fabricacion': 'Año de Fabricación',
            'color': 'Color del Vehículo',
            'patente': 'Patente del Vehículo',
            'num_chasis': 'Número de Chasis',
            'num_motor': 'Número de Motor',
            'estado': 'Estado del Vehículo',
            'kilometraje': 'Kilometraje',
        }
        help_texts = {
            'descripcion': 'Proporcione una descripción breve del vehículo.',
            'anio_fabricacion': 'Ingrese el año de fabricación del vehículo.',
            'color': 'Indique el color del vehículo.',
            'patente': 'Ingrese la patente del vehículo.',
            'num_chasis': 'Proporcione el número de chasis del vehículo.',
            'num_motor': 'Proporcione el número de motor del vehículo.',
            'estado': 'Indique el estado actual del vehículo.',
            'kilometraje': 'Indique el kilometraje actual del vehículo.',
        }

    def clean_anio_fabricacion(self):
        anio_fabricacion = self.cleaned_data.get('anio_fabricacion')
        if anio_fabricacion is not None and (anio_fabricacion < 1886 or anio_fabricacion > 2024):
            raise ValidationError('El año de fabricación debe ser entre 1886 y 2024.')
        return anio_fabricacion

    def clean_estado(self):
        estado = self.cleaned_data.get('estado')
        if not estado:
            raise ValidationError('El estado del vehículo no puede estar vacío.')
        return estado

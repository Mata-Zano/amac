from django import forms
from .models import Tarea, Reporte
from usuarios.models import User
from django.core.exceptions import ValidationError
from datetime import date
from usuarios.models import User, Roles

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'tipo_trabajo', 'fechaFinalizacion', 'asignado_a', 'nota']
        widgets = {
            'fechaFinalizacion': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        operario_rol = Roles.objects.filter(nombre__iexact="operario").first()
        if operario_rol:
            self.fields['asignado_a'].queryset = User.objects.filter(rol=operario_rol)
        else:
            self.fields['asignado_a'].queryset = User.objects.none()

    def clean_fechaFinalizacion(self):
        fecha = self.cleaned_data.get('fechaFinalizacion')
        if fecha and fecha < date.today():
            raise ValidationError("La fecha de finalización no puede ser en el pasado.")
        return fecha





class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = ['asunto', 'mensaje', 'estado', 'tarea']
        widgets = {
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'mensaje': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_estado(self):
        estado = self.cleaned_data.get('estado', False)
        return bool(estado)
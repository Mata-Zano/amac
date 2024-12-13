from django import forms
from .models import Tarea, Reporte
from usuarios.models import User


class TareaForm(forms.ModelForm):
    operario = forms.ModelChoiceField(
        queryset=User.objects.filter(rol__nombre='Operario'),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Asignar a Operario"
    )

    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'nota', 'plazo', 'tipo_trabajo', 'operario']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la Tarea'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción detallada'}),
            'nota': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Notas adicionales'}),
            'plazo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'tipo_trabajo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo de trabajo'}),
        }
        labels = {
            'titulo': 'Título',
            'descripcion': 'Descripción',
            'nota': 'Notas',
            'plazo': 'Plazo',
            'tipo_trabajo': 'Tipo de Trabajo',
        }


class ReporteForm(forms.ModelForm):
    tarea = forms.ModelChoiceField(
        queryset=Tarea.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Tarea Relacionada"
    )

    class Meta:
        model = Reporte
        fields = ['asunto', 'mensaje', 'estado', 'tarea']
        widgets = {
            'asunto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Asunto del reporte'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Detalles del reporte'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'asunto': 'Asunto',
            'mensaje': 'Mensaje',
            'estado': 'Estado (Cerrado/Abierto)',
        }
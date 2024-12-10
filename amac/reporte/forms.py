from django import forms
from .models import Tarea, Reporte

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'nota', 'plazo', 'tipo_trabajo', 'planificador', 'operario']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'nota': forms.Textarea(attrs={'class': 'form-control'}),
            'plazo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'tipo_trabajo': forms.TextInput(attrs={'class': 'form-control'}),
            'planificador': forms.Select(attrs={'class': 'form-control'}),
            'operario': forms.Select(attrs={'class': 'form-control'}),
        }


class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = ['asunto', 'mensaje', 'estado', 'tarea']
        widgets = {
            'asunto': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tarea': forms.Select(attrs={'class': 'form-control'}),
        }

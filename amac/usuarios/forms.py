from django import forms
from django.contrib.auth.hashers import make_password
from usuarios.models import User

class FormUser(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False,  # No obligatorio al editar
        label="Contraseña"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False,  # No obligatorio al editar
        label="Confirmar Contraseña"
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'rol', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'rol': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

from django import forms
from django.contrib.auth.hashers import make_password
from usuarios.models import User, Roles

class UsuarioForm(forms.ModelForm):
    rol = forms.ModelChoiceField(
        queryset=Roles.objects.all(),
        empty_label="Seleccione un Rol",
        widget=forms.Select(attrs={'class': 'user-select'}),
        label="Rol del Usuario"
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'rol', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'user-input-text', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'user-input-text', 'placeholder': 'Apellido'}),
            'username': forms.TextInput(attrs={'class': 'user-input-text', 'placeholder': 'Nombre de Usuario'}),
            'email': forms.EmailInput(attrs={'class': 'user-input-text', 'placeholder': 'Correo Electrónico'}),
            'password': forms.PasswordInput(attrs={'class': 'user-input-text', 'placeholder': 'Contraseña'}),
        }
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'username': 'Nombre de Usuario',
            'email': 'Correo Electrónico',
            'rol': 'Rol del Usuario',
            'password': 'Contraseña',
        }
        help_texts = {
            'username': 'Ingrese un nombre de usuario único.',
            'password': 'Ingrese una contraseña segura.',
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            return make_password(password) 
        return password
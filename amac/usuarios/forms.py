from django import forms
from usuarios.models import User

class FormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','password','rol','email')
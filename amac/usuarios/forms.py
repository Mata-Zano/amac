from django import forms
from usuarios.models import User

class FormUser(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('first_name','last_name','username','rol','email')
        exclude = ('password',)
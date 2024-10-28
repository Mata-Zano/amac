from django.shortcuts import render
from usuarios.models import User

def user (request):
    usuarios = User.objects.all()
    data = {'usuarios': usuarios}
    return render(request, 'listado.html',data)

# Create your views here.

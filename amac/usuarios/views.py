from django.shortcuts import render,redirect, get_object_or_404
from usuarios.models import *
from usuarios.forms import UsuarioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages


@login_required
def user(request):
    usuarios = User.objects.all()
    return render(request, 'listado.html', {'usuarios': usuarios})

@login_required
def addUser(request):
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)
        if usuario_form.is_valid():
            usuario_form.save()
            messages.success(request, 'Usuario creado correctamente.')
            return redirect('User')
    else:
        usuario_form = UsuarioForm()
    return render(request, 'agregar.html', {'usuario_form': usuario_form})
  
@login_required
def editUser(request, id):
    usuario = get_object_or_404(User, id=id)
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST, instance=usuario)
        if usuario_form.is_valid():
            usuario_form.save()
            messages.success(request, 'Usuario actualizado correctamente.')
            return redirect('User')
    else:
        usuario_form = UsuarioForm(instance=usuario)
    return render(request, 'agregar.html', {'usuario_form': usuario_form})


@login_required
def deleteUser(request, id):
    usuario = get_object_or_404(User, id=id)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado correctamente.')
        return redirect('User')
    return render(request, '', {'usuario': usuario})

# Create your views here.

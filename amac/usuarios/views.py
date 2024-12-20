from django.shortcuts import render,redirect
from usuarios.models import *
from usuarios.forms import FormUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages


@login_required
def user(request):
    usuarios = User.objects.all()
    rol = Roles.objects.all()
    data ={
            'usuarios': usuarios,
            'rols': rol
        }
    
    return render(request, 'listado.html', data)

@login_required
def addUser (request):
    form = FormUser()
    if request.method == 'POST' :
        form = FormUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Usuario creado correctamente.')
        return redirect('/')
    data = {'form' : form}
    return render(request, 'agregar.html', data)
  
@login_required
def editUser(request, id):
    usuario = User.objects.get(id = id)
    form = FormUser(instance=usuario)
    if request.method == 'POST' :
        form = FormUser(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario editado correctamente.')
        return redirect('/')
    data = {'form':form}
    return render(request, 'agregar.html', data)


@login_required
def deleteUser(request, id):
    usuario = User.objects.get(id = id)
    usuario.delete()
    messages.success(request, 'Usuario eliminado correctamente.')
    return redirect('/')

# Create your views here.

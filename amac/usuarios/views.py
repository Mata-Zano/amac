from django.shortcuts import render,redirect
from usuarios.models import User
from usuarios.forms import FormUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages


@login_required
def user(request):
    usuarios = User.objects.all()
    data = [
        {
            'id': usuario.id,
            'nombre': f"{usuario.first_name} {usuario.last_name}",
            'email': usuario.email,
            'rol': usuario.rol.nombre if usuario.rol else "Sin asignar"
        }
        for usuario in usuarios
    ]
    return render(request, 'listado.html', {'usuarios': data})

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
    usuario = User.objects.get(id=id)  
    form = FormUser(instance=usuario)

    if request.method == 'POST':
        form = FormUser(request.POST, instance=usuario)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            if password:  # Si se proporciona una nueva contraseña
                user.password = make_password(password)
            user.save()
            messages.success(request, 'Usuario editado correctamente.')
            return redirect('/')  
        else:
            messages.error(request, 'Error al actualizar el usuario.')

    data = {'form': form}
    return render(request, 'agregar.html', data)

def deleteUser(request, id):
    usuario = User.objects.get(id = id)
    usuario.delete()
    messages.success(request, 'Usuario eliminado correctamente.')
    return redirect('/')

# Create your views here.

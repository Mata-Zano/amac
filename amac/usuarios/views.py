from django.shortcuts import render,redirect
from usuarios.models import User
from usuarios.forms import FormUser



def user (request):
    usuarios = User.objects.all()
    data = {'usuarios': usuarios}
    return render(request, 'listado.html',data)

def addUser (request):
    form = FormUser()
    if request.method == 'POST' :
        form = FormUser(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    data = {'form' : form}
    return render(request, 'agregar.html', data)   

def editUser(request, id):
    usuario = User.objects.get(id = id)
    form = FormUser(instance=usuario)
    if request.method == 'POST' :
        form = FormUser(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
        return redirect('/')
    data = {'form':form}
    return render(request, 'agregar.html', data)

def deleteUser(request, id):
    usuario = User.objects.get(id = id)
    usuario.delete()
    return redirect('/')

# Create your views here.

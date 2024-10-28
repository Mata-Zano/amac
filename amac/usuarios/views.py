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
# Create your views here.

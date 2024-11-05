from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from inventario.models import *
from inventario.forms import *
from django.db import transaction


@login_required
def productos (request):
    productos = Inventario.objects.all()
    data = {'productos': productos}
    return render(request, 'listadoP.html',data)

@login_required
def addTipo (request):
    form = TipoForm()
    if request.method == 'POST' :
        form = TipoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    data = {'form' : form}
    return render(request, 'agregarT.html', data)

@login_required
def agregarProducto(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        inventario_form = InventarioForm(request.POST)
        
        if producto_form.is_valid() and inventario_form.is_valid():
            with transaction.atomic():
                producto = producto_form.save()
                inventario = inventario_form.save(commit=False)
                inventario.producto = producto
                inventario.save()
            return redirect('/')
        else:
            data ={
        'producto_form': producto_form,
        'inventario_form': inventario_form
        }
    else:
        producto_form = ProductoForm()
        inventario_form = InventarioForm()
        data ={
        'producto_form': producto_form,
        'inventario_form': inventario_form
        }
    return render(request, 'agregarP.html',data)
  

# Create your views here.

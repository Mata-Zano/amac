from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Vehiculo, Marca, Modelo
from .forms import *
from django.contrib.auth.decorators import login_required
import os

@login_required
def registro_vehiculo(request):
    if request.method == 'POST':
        vehiculo_form = VehiculoForm(request.POST)
        if vehiculo_form.is_valid():
            vehiculo_form.save()
            return redirect('vehiculo_lista')
    else:
        vehiculo_form = VehiculoForm()
    return render(request, 'registro_vehiculo.html', {'vehiculo_form': vehiculo_form})

@login_required
def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    marca = Marca.objects.all()
    vehiculo_form = VehiculoForm()
    modelo_form = ModeloForm()
    marca_form = MarcaForm()

    data ={
        'vehiculos': vehiculos,
        'marcas': marca,
        'vehiculo_form': vehiculo_form,
        'modelo_form': modelo_form,
        'marca_form': marca_form
        
    }
    return render(request, 'lista_vehiculos.html', data)

@login_required
def addMarca(request):
    form = MarcaForm()
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehiculo_lista')
    return render(request, 'formMarca.html', {'form': form})

@login_required
def addModelo (request):
    form = ModeloForm()
    if request.method == 'POST' :
        form = ModeloForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('vehiculo_lista')
    data = {'form' : form}
    return render(request, 'formModelo.html', data)

@login_required
def deleteVehiculo(request, id):
    vehiculo = Vehiculo.objects.get(id=id)
    vehiculo.delete()
    # if vehiculo.imagen:  # Verifica si el vehiculo tiene una imagen
    #     try:
    #         if os.path.isfile(vehiculo.imagen.path):
    #             os.remove(vehiculo.imagen.path)
    #     except ValueError:
    #         pass
        
    return redirect('/lista/')
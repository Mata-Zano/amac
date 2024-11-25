from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Vehiculo, Marca, Modelo
from .forms import VehiculoForm

def registro_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehiculo_lista')
    else:
        form = VehiculoForm()
    return render(request, 'registro_vehiculo.html', {'form': form})

def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'lista_vehiculos.html', {'vehiculos': vehiculos})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from mantencion.forms import *
from .forms import VehiculoForm
from django.forms import inlineformset_factory
from django.forms import modelformset_factory
@login_required

def mantencion(request):
    # Formulario de cada entidad
    formMantencion = MantencionForm()
    servicioForm = ServicioForm()
    vehiculoForm = VehiculoForm()
    modeloForm = ModeloForm()
    marcaForm = MarcaForm()

    if request.method == 'POST':
        # Crear el formulario de cada entidad
        formMantencion = MantencionForm(request.POST)
        servicio = ServicioForm(request.POST)  
        vehiculo = VehiculoForm(request.POST)
        modelo = ModeloForm(request.POST)
        marca = MarcaForm(request.POST)

        if marca.is_valid():  # Primero, guarda la marca
            marca_instance = marca.save()  # Guarda la marca y obtiene su instancia

            # Crea el modelo asociado a la marca
            if modelo.is_valid():
                modelo.instance.marca = marca_instance  # Asocia el modelo con la marca
                modelo.save()  # Guarda el modelo

                # Crea el vehículo asociado al modelo y la marca
                if vehiculo.is_valid():
                    vehiculo.instance.marca = marca_instance  # Asocia el vehículo con la marca
                    vehiculo.instance.modelo = modelo.instance  # Asocia el vehículo con el modelo
                    vehiculo.save()  # Guarda el vehículo

                    # Finalmente, crea la mantención usando el vehículo
                    if formMantencion.is_valid():
                        formMantencion.instance.vehiculo = vehiculo.instance  # Asocia la mantención con el vehículo
                        formMantencion.save()  # Guarda la mantención

            # Redirige a otra vista o muestra un mensaje de éxito
            return redirect('lista/')  # Cambia a la URL de tu elección

    # Datos para renderizar la página
    data = {
        'formMantencion': formMantencion,
        'formVehiculo': vehiculoForm,
        'modeloForm': modeloForm,
        'marcaForm': marcaForm,
        'productoenMantencionFomr': ProductoEnMantencionForm(),
    }

    return render(request, 'mantencion.html', data)

   # Crear formulario para Mantencion
    # MantencionFormSet = modelformset_factory(ProductoEnMantencion, form=ProductoEnMantencionForm, extra=1, can_delete=True)
    
    # if request.method == 'POST':
    #     mantencion_form = MantencionForm(request.POST)
    #     productos_formset = MantencionFormSet(request.POST, queryset=ProductoEnMantencion.objects.none())

    #     if mantencion_form.is_valid() and productos_formset.is_valid():
    #         # Guardar mantención
    #         mantencion = mantencion_form.save()

    #         # Guardar productos relacionados
    #         for producto_form in productos_formset:
    #             if producto_form.cleaned_data:  # Evitar guardar formularios vacíos
    #                 producto = producto_form.save(commit=False)
    #                 producto.mantencion = mantencion
    #                 producto.save()

    #         return redirect('mantencion')  # Redirigir al listado de mantenciones

    # mantencion_form = MantencionForm()
    # productos_formset = MantencionFormSet(queryset=ProductoEnMantencion.objects.none())

    # return render(request, 'mantencion.html', {
    #     'mantencion_form': mantencion_form,
    #     'productos_formset': productos_formset,
    # })

# @login_required
# def addProductMantencion(request):
#     # Obtener el último ID de Mantencion y calcular el próximo
#     last_mantencion = Mantencion.objects.order_by('id').last()  # Última mantención
#     next_id = last_mantencion.id + 1 if last_mantencion else 1  # Próximo ID

#     # Verificar si existe una mantención con este ID
#     mantencion, created = Mantencion.objects.get_or_create(id=next_id)

#     form = ProductoEnMantencionForm()
#     data = {'productid': next_id}  # Pasar el próximo ID al template

#     if request.method == 'POST':
#         form = ProductoEnMantencionForm(request.POST)
#         if form.is_valid():
#             product = form.save(commit=False)  # No guardar aún
#             product.mantencion = mantencion  # Asignar la mantención existente o creada
#             product.save()  # Guardar el producto asociado
#             return redirect('mantencion')

#     return render(request, 'agregarProducto.html', {'form': form, 'data': data})


# @login_required
# def addMantencion(request):
#     last_mantencion = Mantencion.objects.order_by('id').last()  # Última mantención
#     form = MantencionForm()
#     if request.method == 'POST':
#         form = MantencionForm(request.POST)
#         if form.is_valid():
#             mantencion = form.save(commit=False)  # No guardar aún
#             mantencion.id = last_mantencion
#             mantencion.save()
#             return redirect('mantencion')
#         return redirect('mantencion')

# @login_required
# def servicios(request): 
    
#     return render(request, 'servicios.html')


# # Create your views here.

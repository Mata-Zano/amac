from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea, Reporte
from .forms import TareaForm, ReporteForm
from django.contrib.auth.decorators import login_required


# TAREAS
# Lista Tareas
@login_required
def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'lista_tareas.html', {'tareas': tareas})

# Agregar Tarea
@login_required
def agregar_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.creado_por = request.user  
            tarea.save()
            return redirect('lista_tareas')  
        else:
            print(form.errors)  
    else:
        form = TareaForm()
    return render(request, 'agregar_tarea.html', {'form': form})

# Editar Tarea
@login_required
def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)

    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()  
            return redirect('lista_tareas')  
    else:
        form = TareaForm(instance=tarea)

    return render(request, 'agregar_tarea.html', {'form': form, 'tarea': tarea})

# Eliminar Tarea
@login_required
def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.delete()
    return redirect('lista_tareas')



# REPORTES
# Lista Reportes
@login_required
def lista_reportes(request):
    reportes = Reporte.objects.all()
    return render(request, 'lista_reportes.html', {'reportes': reportes})

# Crear Reporte
@login_required
def agregar_reporte(request):
    if request.method == 'POST':
        form = ReporteForm(request.POST)
        if form.is_valid():
            reporte = form.save(commit=False)
            reporte.creado_por = request.user  # Asigna el usuario actual como creador
            reporte.save()
            return redirect('lista_reportes')
    else:
        form = ReporteForm()
    return render(request, 'agregar_reporte.html', {'form': form})

# Editar Reporte
login_required
def editar_reporte(request, reporte_id):
    reporte = get_object_or_404(Reporte, id=reporte_id)
    if request.method == 'POST':
        form = ReporteForm(request.POST, instance=reporte)
        if form.is_valid():
            reporte = form.save(commit=False)
            reporte.estado = request.POST.get('estado', 'off') == 'on'
            reporte.save()
            return redirect('lista_reportes')
    else:
        form = ReporteForm(instance=reporte)
    return render(request, 'agregar_reporte.html', {'form': form, 'reporte': reporte})

# Eliminar Reporte
@login_required
def eliminar_reporte(request, reporte_id):
    reporte = get_object_or_404(Reporte, id=reporte_id)
    reporte.delete()
    return redirect('lista_reportes')

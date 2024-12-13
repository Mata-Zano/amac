from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Tarea, Reporte
from .forms import TareaForm, ReporteForm
from .decorators import es_planificador, es_operario, es_admin

@login_required 
@es_planificador
def lista_tareas(request):
    tareas = Tarea.objects.filter(planificador=request.user)
    return render(request, 'reportes/lista_tareas.html', {'tareas': tareas})


@login_required
@es_planificador
def agregar_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.planificador = request.user  # Asigna automáticamente al usuario actual como planificador
            tarea.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    return render(request, 'reportes/agregar_tarea.html', {'form': form})



@login_required
@es_operario
def lista_tareas_operario(request):
    tareas = Tarea.objects.filter(operario=request.user)
    return render(request, 'reportes/lista_tareas_operario.html', {'tareas': tareas})


@login_required
@es_operario
def agregar_reporte(request):
    if request.method == 'POST':
        form = ReporteForm(request.POST)
        if form.is_valid():
            reporte = form.save(commit=False)
            reporte.creador = request.user  # Asigna al usuario actual como creador del reporte
            reporte.save()
            return redirect('lista_reportes_operario')
    else:
        form = ReporteForm()
    return render(request, 'reportes/agregar_reporte.html', {'form': form})



@login_required
@es_admin
def lista_reportes(request):
    reportes = Reporte.objects.all()
    return render(request, 'reportes/lista_reportes.html', {'reportes': reportes})

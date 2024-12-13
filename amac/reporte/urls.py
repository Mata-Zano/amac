from django.urls import path
from .views import *

urlpatterns = [
    path('tareas/', lista_tareas, name='lista_tareas'),
    path('tareas/agregar/', agregar_tarea, name='agregar_tarea'),
    path('tareas/operario/', lista_tareas_operario, name='lista_tareas_operario'),
    path('reportes/agregar/', agregar_reporte, name='agregar_reporte'),
    path('reportes/', lista_reportes, name='lista_reportes'),
]

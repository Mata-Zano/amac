from django.urls import path
from .views import *

urlpatterns = [
    path('tareas/', lista_tareas, name='lista_tareas'),
    path('tareas/agregar/', agregar_tarea, name='agregar_tarea'),
    path('tareas/editar/<int:tarea_id>/', editar_tarea, name='editar_tarea'),
    path('tareas/eliminar/<int:tarea_id>/', eliminar_tarea, name='eliminar_tarea'),

    path('reportes/', lista_reportes, name='lista_reportes'),
    path('reportes/agregar/', agregar_reporte, name='agregar_reporte'),
    path('reportes/editar/<int:reporte_id>/', editar_reporte, name='editar_reporte'),
    path('reportes/eliminar/<int:reporte_id>/', eliminar_reporte, name='eliminar_reporte'),
]
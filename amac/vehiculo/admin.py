from django.contrib import admin
from .models import Vehiculo, Marca, Modelo

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais_origen')
   

admin.site.register(Marca, MarcaAdmin)

class ModeloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'version', 'motor', 'marca')
    
    

admin.site.register(Modelo, ModeloAdmin)

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'anio_fabricacion', 'color', 'patente', 'num_chasis', 'num_motor', 'estado', 'marca', 'modelo')
    

admin.site.register(Vehiculo, VehiculoAdmin)



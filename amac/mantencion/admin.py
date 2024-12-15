from django.contrib import admin
from .models import *

class Servicios (admin.ModelAdmin):
    list_display = ("*")


admin.site.register(Servicio)
admin.site.register(Mantencion)
admin.site.register(ProductoUtilizado)


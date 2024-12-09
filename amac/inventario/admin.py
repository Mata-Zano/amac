from django.contrib import admin
from .models import *

class TipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

admin.site.register(Tipo, TipoAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'descripcion')
    list_filter = ('tipo',)
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)

admin.site.register(Producto, ProductoAdmin)

class InventarioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'stock', 'fechaIngreso', 'fechaVencimiento', 'stockMinimo')
    list_filter = ('fechaIngreso', 'fechaVencimiento')
    search_fields = ('producto__nombre',)
    ordering = ('producto',)

admin.site.register(Inventario, InventarioAdmin)

admin.site.register(Proveedor)
admin.site.register(modelo)

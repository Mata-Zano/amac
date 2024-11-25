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
    list_display = ('producto', 'stock', 'fecha_ingreso', 'fecha_vencimiento', 'stock_minimo')
    list_filter = ('fecha_ingreso', 'fecha_vencimiento')
    search_fields = ('producto__nombre',)
    ordering = ('producto',)

admin.site.register(Inventario, InventarioAdmin)
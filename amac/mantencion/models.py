from django.db import models
from vehiculo.models import *
from usuarios.models import *
from inventario.models import *
from mantencion.models import *
from reporte.models import *

class Servicio(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    precio = models.IntegerField(null=True,)
    duracion = models.DurationField(null=True, blank=True)  # Opcional
    def __str__(self):
        return self.nombre


class Mantencion(models.Model):
    class Estado(models.TextChoices):
        COTIZACION = 'Cotizacion', 'Cotización'
        COTIZACION_AUTORIZADA = 'Cotizacion Autorizada', 'Cotización Autorizada'
        COMPLETADA = 'Completada', 'Completada'
        EN_PROCESO = 'En Proceso', 'En Proceso'
        DESCARTADA = 'Descartada', 'Descartada'
        REVISION = 'Revision', 'Revisión'

    fecha = models.DateField(auto_now_add=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    reporte = models.ForeignKey(Reporte, on_delete=models.CASCADE, null=True)
    recepcionista = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tarea = models.ForeignKey(Tarea,blank=True, on_delete=models.CASCADE, null=True)
    revision_inicial = models.CharField(max_length=650, null=True, blank=True)
    servicio = models.ManyToManyField(Servicio, blank=True)
    precio_total = models.IntegerField(null=True,)
    otroServicio = models.CharField(max_length=100, null=True, blank=True)
    productosUtilizado = models.ManyToManyField(Producto,blank=True, through='ProductoEnMantencion')
    estado = models.CharField(
        max_length=50, 
        choices=Estado.choices, 
        default=Estado.COTIZACION
    )


    def __str__(self):
        return f"Mantención {self.id} - {self.vehiculo}"
    
class ProductoEnMantencion(models.Model):
    mantencion = models.ForeignKey(Mantencion, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, null=True)


class ProductoUtilizado(models.Model):
    mantencion = models.ForeignKey(Mantencion, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=True)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad} unidades"

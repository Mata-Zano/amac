from django.db import models

class Tipo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Inventario(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE)
    stock = models.IntegerField()
    fecha_ingreso = models.DateField()
    fecha_vencimiento = models.DateField()
    stock_minimo = models.IntegerField()
    
    def __str__(self):
        return f"Inventario de {self.producto.nombre}"
# Create your models here.

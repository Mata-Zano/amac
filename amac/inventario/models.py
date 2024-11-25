from typing import Any
from django.db import models
import os 
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100,null=True)
    direccion = models.CharField(max_length=250,null=True)
    telefono = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    pais = models.CharField(max_length=100,null=True)
    ciudad = models.CharField(max_length=100,null=True)
    estado = models.BooleanField(default=True,null=True)
    contactoPrincipa = models.CharField(max_length=100,null=True)
    nombreContacto = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.nombre

class modelo(models.Model):
    nombre = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.nombre

class Tipo(models.Model):
    nombre = models.CharField(max_length=255,null=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
    def nombreProveedor(self):
        return f"{self.nombre}"

class Producto(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100,null=True)
    descripcion = models.TextField(null=True)
    marca = models.CharField(max_length=100,null=True)
    modeloCompatible = models.ManyToManyField(modelo)
    unidadMedida = models.CharField(max_length=100,null=True)
    imagen = models.ImageField(blank=True, upload_to='productos/')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True)



    def verificarCompatibilidad(self, modelo):
        if modelo in self.modeloCompatible:
            return True
        else:   
            return False    
        
    def __str__(self):
        return self.nombre


class Inventario(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE)
    stock = models.IntegerField(null=True)
    fechaIngreso = models.DateField(auto_now_add=True ,null=True)
    fechaVencimiento = models.DateField(null=True)
    stockMinimo = models.IntegerField(default=0)
    ultimaSalida = models.DateField(null=True)
    ubicacion = models.CharField(max_length=250, null=True )
    estado = models.BooleanField(default=True)


    

    def __str__(self):
        estado_str = "Disponible" if self.estado else "No disponible"
        return f"Inventario de {self.producto.nombre} - {estado_str}"

# Create your models here.

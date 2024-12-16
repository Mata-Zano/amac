from django.db import models
from usuarios.models import User
from datetime import date

class Tarea(models.Model):
    titulo = models.CharField(max_length=255)
    fechaCreacion = models.DateField(auto_now_add=True)  # Fecha automática al crear
    descripcion = models.TextField()
    estado = models.BooleanField(default=False)  # Completada o no
    nota = models.TextField(blank=True, null=True)
    plazo = models.IntegerField(blank=True, null=True)  # Calculado automáticamente como días
    fechaFinalizacion = models.DateField(blank=True, null=True)
    tipo_trabajo = models.CharField(max_length=100)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas_creadas')  
    asignado_a = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas_asignadas', null=True, blank=True)  # Operario asignado

    def save(self, *args, **kwargs):
        if not self.fechaCreacion:
            self.fechaCreacion = date.today()

        if self.fechaFinalizacion and self.fechaCreacion:
            self.plazo = (self.fechaFinalizacion - self.fechaCreacion).days

        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo


class Reporte(models.Model):
    asunto = models.CharField(max_length=255)
    fecha_creacion = models.DateField(auto_now_add=True)
    mensaje = models.TextField()
    estado = models.BooleanField(default=False)  # Cerrado o abierto
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='reportes')
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reportes_creados') 

    def __str__(self):
        return f"{self.asunto} - {self.tarea.titulo}"

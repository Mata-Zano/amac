from django.db import models
from django.conf import settings

class Tarea(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    estado = models.BooleanField(default=False)  # Completada o no
    nota = models.TextField(blank=True, null=True)
    plazo = models.DateField()
    fecha_finalizacion = models.DateField(blank=True, null=True)
    tipo_trabajo = models.CharField(max_length=100)
    planificador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='tareas_asignadas',
        on_delete=models.CASCADE
    )
    operario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='tareas_recibidas',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.titulo


class Reporte(models.Model):
    asunto = models.CharField(max_length=255)
    fecha_creacion = models.DateField(auto_now_add=True)
    mensaje = models.TextField()
    estado = models.BooleanField(default=False)  # Cerrado o abierto
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='reportes')
    creador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reportes_creados'
    )

    def __str__(self):
        return f"{self.asunto} - {self.tarea.titulo}"

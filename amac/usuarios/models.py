from django.db import models

class roles (models.Model):
    nombre = models.CharField(max_length=30,  null= False, unique=True, verbose_name='Nombre')

    def __str__(self):
        return self.nombre
    
    class Meta: 
        db_table = 'rol'
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

# Create your models here.
    
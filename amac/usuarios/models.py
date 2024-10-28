from django.db import models
from django.contrib.auth.models import AbstractUser




class Roles (models.Model):
    nombre = models.CharField(max_length=30,  null= False, unique=True, verbose_name='Nombre')

    def __str__(self):
        return self.nombre
    
    class Meta: 
        db_table = 'rol'
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'


class User(AbstractUser):
    rol = models.ForeignKey(Roles, null=False, blank=False, on_delete= models.DO_NOTHING)
# Create your models here.

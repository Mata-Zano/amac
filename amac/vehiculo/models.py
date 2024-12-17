from django.db import models

# Create your models here.


class Marca(models.Model):
    PAISES_CHOICES = [
        ('japon', 'Japón'),
        ('corea_del_sur', 'Corea del Sur'),
        ('alemania', 'Alemania'),
        ('estados_unidos', 'Estados Unidos'),
        ('china', 'China'),
        ('francia', 'Francia'),
        ('italia', 'Italia'),
    ]

    nombre = models.CharField(max_length=100)
    pais_origen = models.CharField(
        max_length=50,
        choices=PAISES_CHOICES,
        )

    def __str__(self):
        return self.nombre

    def mostrar_detalle(self):
        return f"Marca: {self.nombre}, País de Origen: {self.pais_origen}"

    def actualizar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        self.save()

    def actualizar_pais_origen(self, nuevo_pais_origen):
        self.pais_origen = nuevo_pais_origen
        self.save()

class Modelo(models.Model):
    TIPO_CHOICES = [
        ('auto', 'Automóvil'),
        ('suv', 'SUV'),
        ('camioneta', 'Camioneta'),
        ('jeep', 'Jeep'),
        ('camion', 'Camión'),
        ('bus', 'Bus'),
        ('minivan', 'Minivan'),
        ('maquinaria', 'Maquinaria Pesada'),
        ('pickup', 'Pick-Up'),
        ('furgon', 'Furgón'),
        ('minibus', 'Minibús'),
    ]
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=1000, choices=TIPO_CHOICES)
    version = models.CharField(max_length=100)
    motor = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='modelos')

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

    def mostrar_detalle(self):
        return f"Modelo: {self.nombre},  Tipo: {self.tipo}, Versión: {self.version}, Motor: {self.motor}"

    def actualizar_version(self, nueva_version):
        self.version = nueva_version    
        self.save()

    def actualizar_motor(self, nuevo_motor):
        self.motor = nuevo_motor
        self.save()

    def actualizar_tipo(self, nuevo_tipo):
        self.tipo = nuevo_tipo
        self.save()

class Vehiculo(models.Model):

    ESTADO_CHOICES = [
        ('buen_estado', 'Buen Estado'),
        ('estado_regular', 'Estado Regular'),
        ('mal_estado', 'Mal Estado'),
    ]

    descripcion = models.CharField(max_length=50)
    anio_fabricacion = models.IntegerField()
    color = models.CharField(max_length=50)
    kilometraje = models.IntegerField()
    patente = models.CharField(max_length=10)
    num_chasis = models.CharField(max_length=50)
    num_motor = models.CharField(max_length=50)
    estado = models.CharField(
        max_length=50,
        choices=ESTADO_CHOICES,
        )
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    
    

    def __str__(self):
        return f"{self.marca.nombre} {self.modelo.nombre} ({self.patente})"
class Cliente(models.Model): 
    razon_social = models.CharField(max_length=255, null=True) 
    rut = models.CharField(max_length=20, unique=True, null=True) 
    direccion = models.CharField(max_length=255, null=True) 
    telefono = models.CharField(max_length=15, null=True) 
    email = models.EmailField() 
    nombre_contacto = models.CharField(max_length=255, null=True) 
    cargo_contacto = models.CharField(max_length=255, null=True) 
    estado = models.CharField(max_length=50, choices=(('activo', 'Activo'), ('inactivo', 'Inactivo')), null=True) 
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, null=True)
    def mostrar_informacion(self): 
        return f'{self.razon_social} ({self.rut}) - Contacto: {self.nombre_contacto}' 
    
    def __str__(self): 
        return self.razon_social

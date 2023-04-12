from django.db import models
from datetime import datetime

# Create your models here.

class Tipo(models.Model):
    tipo = models.CharField(max_length=150, verbose_name='Tipo Usuario')
     
    def __str__(self) -> str:
        return self.tipo
     
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural='Tipos'
        db_table = 'Tipos'
        ordering = ['id']
     

class Piloto(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, related_name='Tipos')
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    apellido = models.CharField(max_length=150, verbose_name='Apellido')
    identificacion = models.CharField(max_length=10, unique=True, verbose_name='Cédula')
    fecha_registro = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    fecha_creacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de creación')
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de actualización')
    edad = models.PositiveIntegerField(default=0)
    stado = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"
    
    class Meta:
        verbose_name = 'Piloto'
        verbose_name_plural='Pilotos'
        db_table = 'Pilotos'
        ordering = ['id']


class Vuelo(models.Model):
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE, related_name='Vuelos')
    fecha = models.DateField()
    hora_despegue = models.TimeField()
    hora_aterrizaje = models.TimeField()
    duracion_minutos = models.IntegerField()
    descripcion = models.TextField()
    creado_por = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fecha} ({self.piloto})"

    class Meta:
            verbose_name = 'Vuelo'
            verbose_name_plural='VUelos'
            db_table = 'Vuelos'
            ordering = ['id']


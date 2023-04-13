from django.db import models
from datetime import datetime
from django.forms import model_to_dict

# Create your models here.
     
class Piloto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    apellido = models.CharField(max_length=150, verbose_name='Apellido')
    identificacion = models.CharField(max_length=10, unique=True, verbose_name='Cédula')
    fecha_registro = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    fecha_creacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de creación')
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de actualización')
    edad = models.PositiveIntegerField(default=0)
    estado = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"
    
    class Meta:
        verbose_name = 'Piloto'
        verbose_name_plural='Pilotos'
        db_table = 'Pilotos'
        ordering = ['id']
    
    def toJSON(self):
         item = model_to_dict(self)
         return item

class Vuelo(models.Model):
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE, related_name='Vuelos')
    fecha = models.DateField()
    hora_despegue = models.TimeField()
    hora_aterrizaje = models.TimeField()
    duracion_minutos = models.IntegerField()
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fecha} ({self.piloto})"

    class Meta:
            verbose_name = 'Vuelo'
            verbose_name_plural='Vuelos'
            db_table = 'Vuelos'
            ordering = ['id']

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Myapp(models.Model):
    field1 = models.CharField(max_length=255)
    field2 = models.CharField(max_length=255)

class Sugerencias(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Revisada', 'Revisada'),
        ('Implementada', 'Implementada'),
    ]
    sugerencia = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado= models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')
    def __str__(self):
        return self.sugerencia
    class Meta:
        verbose_name_plural = "Sugerencias"

class Event(models.Model):
    title = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.title
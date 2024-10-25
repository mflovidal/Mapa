from django.db import models

# Create your models here.
class Myapp(models.Model):
    field1 = models.CharField(max_length=255)
    field2 = models.CharField(max_length=255)
# marcador
class Marcador(models.Model):
    nombre = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()
    imagen = models.ImageField(upload_to='')  
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

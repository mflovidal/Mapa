from django.db import models

# Create your models here.
class Myapp(models.Model):
    field1 = models.CharField(max_length=255)
    field2 = models.CharField(max_length=255)

class Sugerencias(models.Model):
    sugerencia = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sugerencia
    class Meta:
        verbose_name_plural = "Sugerencias"
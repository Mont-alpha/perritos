from django.db import models
import os

# Create your models here.
class Perrito(models.Model):
    NIVELES_ENERGIA = [
        ('baja', 'Baja'),
        ('alta', 'Alta'),
    ]

    SEXO = [
        ('macho', 'Macho'),
        ('hembra', 'Hembra'),
    ]

    TAMANOS = [
        ('pequeño', 'Pequeño'),
        ('mediano', 'Mediano'),
        ('grande', 'Grande'),
    ]

    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    nivel_energia = models.CharField(max_length=4, choices=NIVELES_ENERGIA)
    sexo = models.CharField(max_length=6, choices=SEXO)
    tamano = models.CharField(max_length=7, choices=TAMANOS)
    es_adopcion_doble = models.OneToOneField('Perrito', on_delete=models.DO_NOTHING,null=True, blank=True)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='perritos/')
    
    def delete(self, *args, **kwargs):
        if self.imagen and os.path.isfile(self.imagen.path):
            os.remove(self.imagen.path)  # Eliminar la imagen del sistema
        super().delete(*args, **kwargs)  # Eliminar el objeto de la base de datos
    
    def __str__(self):
        return f"{self.nombre} - {self.sexo} - {self.tamano}"
from django.db import models

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
    es_adopcion_doble = models.BooleanField(default=False)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='perritos/')
    
    def __str__(self):
        return f"{self.nombre} - {self.sexo} - {self.tamano}"
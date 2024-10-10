from django.db import models

# Create your models here.
class perritos(models.Model):
    nombre_perrito = models.CharField(max_length=100)
    edad = models.DateField()
    raza = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
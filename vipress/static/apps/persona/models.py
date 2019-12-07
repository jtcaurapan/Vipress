from django.db import models

# Create your models here.


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    domicilio = models.TextField()
    genero = models.CharField(max_length=10)

class Orador(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    genero = models.CharField(max_length=10)
    Especialidad =models.CharField(max_length=50)

    def __str__(self):
        return '{} {} ({})'.format(self.nombre, self.apellidos, self.Especialidad)

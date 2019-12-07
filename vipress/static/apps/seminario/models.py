from django.db import models
from apps.persona.models import Persona, Orador
# Create your models here.



class Seminario(models.Model):
    titulo = models.CharField(max_length=50)
    duracion = models.DurationField()
    Cantidad_participantes = models.IntegerField()
    fecha = models.DateField()
    direccion = models.TextField()
    orador = models.ManyToManyField(Orador)

from django.db import models

from .managers import AutorManager
# Create your models here

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=20)
    edad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.id) +  ' ' + self.nombre +  ' ' +self.apellidos

    class Meta:
        abstract= True


class Autor(Persona):
    seudonimo = models.CharField('Seudonimo', max_length=50,blank=True)
    

    objects = AutorManager()

    

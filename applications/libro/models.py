from django.db import models
from django.db.models.signals import post_save
from applications.autor.models import Autor

from .managers import LibroManager,CategoriaManager

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=30)

    def __str__(self):
        return str(self.id) + ' - ' +self.nombre

    objects = CategoriaManager()



    

class Libro(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,related_name='categoria_libro')
    #m2m
    autor = models.ManyToManyField(Autor)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField('Fecha de Lanzamiento')
    visitas = models.PositiveIntegerField()
    stock= models.PositiveIntegerField(default=0)


    objects = LibroManager()

    def __str__(self):
        return str(self.id) + ' - ' +self.titulo



'''def prueba_signal(sender, instance, **kwargs):
    print('Prueba de signals')
    print(instance)


post_save.connect(prueba_signal, sender=Libro)'''
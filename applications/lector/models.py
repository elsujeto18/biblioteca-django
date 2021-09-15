from django.db import models
from django.db.models.signals import post_delete, post_save


from applications.libro.models import Libro
from applications.autor.models import Persona

from .managers import PrestamoManager

# Create your models here.



class Lector(Persona):
    class Meta:
        verbose_name='Lector'
        verbose_name_plural ='Lectores'
    


class Prestamo(models.Model):
    #fk djanator
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE,related_name='libro_prestamo')
    fecha_prestamo = models.DateField('Fecha de Prestamo')
    fecha_devolucion = models.DateField('Fecha de Devolución',blank=True, null=True)
    devuelto = models.BooleanField()

    objects = PrestamoManager()

    #esto permite hacer un guardado extra en el administrador, con esto logramos que se disminuya el stock
    def save(self, *args, **kwargs):
        if self.devuelto == False:
            self.libro.stock = self.libro.stock -1
            self.libro.save()
            
        else:
            self.libro.save()

        super(Prestamo, self).save(*args, **kwargs)





    def __str__(self):
        return self.libro.titulo

'''def update_libro_stock(sender, instance, **kwargs):
    #actualizamos el stock si se elimina un prestamo
    instance.libro.stock = instance.libro.stock + 1
    instance.libro.save()


post_delete.connect(update_libro_stock, sender=Prestamo)'''


def update_libro_stock(sender, instance, **kwargs):
    print(instance.devuelto)
    if instance.devuelto == True:
        instance.libro.stock = instance.libro.stock + 1
        instance.libro.save()
    else:
        print('hola')


post_save.connect(update_libro_stock, sender=Prestamo)
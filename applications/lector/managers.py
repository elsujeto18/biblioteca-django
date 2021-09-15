import datetime
from django.db import models
from django.db.models import Q, Count, Avg, Sum
from django.db.models.functions import Lower



class PrestamoManager(models.Manager):
    
    def libros_promedio_edad(self):
        resultado = self.filter(libro__id='3').aggregate(prom_edad=Avg('lector__edad'), sum_edad=Sum('lector__edad'))

        return resultado

    def num_libros_prestados(self):
        resultado = self.values('libro').annotate(num_prestados=Count('libro'),titulo=Lower('libro__titulo'),)

        for r in resultado:
            print(r, r['num_prestados'])

        return resultado
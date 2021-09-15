import datetime
from django.db import models
from django.db.models import Q, Count
from django.contrib.postgres.search import TrigramSimilarity




class LibroManager(models.Manager):
    #managers para el modelo autor
    def listar_libros(self, kword):

        resultado = self.filter(titulo__icontains=kword, fecha__range=('2019-01-01','2020-12-01'))
        return resultado


    #trigram nos permite la busqueda mas eficiente y exacta, siempre deben haber almenos tres caracteres en la busqueda
    def listar_libros_trg(self, kword):
        if kword:
            resultado = self.filter(titulo__trigram_similar=kword)
            return resultado
        else:
            return self.all()

        

    def listar_libros2(self, kword, fecha1, fecha2):

        #esto permite transformar las fechas al formato correcto
        date1 =datetime.datetime.strptime(fecha1, "%Y-%m-%d").date()
        date2 =datetime.datetime.strptime(fecha2, "%Y-%m-%d").date()

        resultado = self.filter(titulo__icontains=kword, fecha__range=(date1,date2))
        return resultado
    

    def listar_libros_byCategoria(self, categoria):
        return self.filter(categoria__id=categoria).order_by('titulo')


    def add_autor_libro(self, libro_id, autor):
        libro = self.get(id=libro_id)
        libro.autor.add(autor)
        return libro
    

    def libros_num_prestamo(self):
        #nos devuelve un diccionario con valor de la operacion aritmetica
        resultado = self.aggregate(num_prestamos=Count('libro_prestamo'))
        return resultado


    def num_libros_prestados(self):
        resultado = self.annotate(num_prestados=Count('libro_prestamo'))

        for r in resultado:
            print(r, r.num_prestados)

        return resultado



    
    
class CategoriaManager(models.Manager):
    #distinct() permite que no se repitan las categorias
    def categoria_por_autor(self, autor):
        return self.filter(categoria_libro__autor__id=autor).distinct()

    # con annotate puedo contar la cantidad de libros que se encuentran en cada categoria
    #nos devulve u queryset y la variable que hace nuestra funcion aritmetica
    def listar_categoria_libros(self):
        resultado = self.annotate(num_libros=Count('categoria_libro'))

        for r in resultado:
            print(r,r.num_libros)
        return resultado

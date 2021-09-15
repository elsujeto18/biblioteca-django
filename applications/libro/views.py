from django.shortcuts import render

from .models import Libro

from django.views.generic import ListView,DetailView

# Create your views here.


class ListLibros(ListView):
   
    context_object_name = 'lista_libros'
    template_name = "libro/lista_libro.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        f1 = self.request.GET.get('fecha1', '')
        f2= self.request.GET.get('fecha2', '')

        if f1 and f2:
            return Libro.objects.listar_libros2(palabra_clave,f1,f2)
        else:
            return Libro.objects.listar_libros(palabra_clave)


class ListLibrosTrg(ListView):
   
    context_object_name = 'lista_libros'
    template_name = "libro/lista_libro.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
    
        return Libro.objects.listar_libros_trg(palabra_clave)




class ListLibros_byCategoria(ListView):
   
    context_object_name = 'lista_libros_by'
    template_name = "libro/lista_libro2.html"

    def get_queryset(self):
        
        return Libro.objects.listar_libros_byCategoria('4')
       
        

class LibroDetailView(DetailView):
    model = Libro
    template_name = "libro/detail.html"

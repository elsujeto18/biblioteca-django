from django.contrib import admin
from django.urls import path


from . import views

urlpatterns = [
    path('libros/', views.ListLibros.as_view(), name='libros'),
    path('libros-bycategoria/', views.ListLibros_byCategoria.as_view(), name='libros-categoria'),
    path('libro-detail/<pk>', views.LibroDetailView.as_view(), name='detail-libro'),
    path('libro-trg/', views.ListLibrosTrg.as_view(), name='libro-trg'),
]
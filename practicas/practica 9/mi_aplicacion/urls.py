# mi_aplicacion/urls.py

from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('test_template', views.test_template, name='test_template'),
  path('lista_autores', views.lista_autores, name='lista_autores'),
  path('anadir_autor', views.anadir_autor, name='anadir_autor'),
  path('borrar_autor', views.borrar_autor, name='borrar_autor'),
  path('modificar_autor/<int:id_autor>', views.modificar_autor, name='modificar_autor'),
  path('lista_libros', views.lista_libros, name='lista_libros'),
  path('anadir_libro', views.anadir_libro, name='anadir_libro'),
  path('borrar_libro', views.borrar_libro, name='borrar_libro'),
  path('modificar_libro/<int:id_libro>', views.modificar_libro, name='modificar_libro'),
  path('lista_prestamos', views.lista_prestamos, name='lista_prestamos'),
  path('anadir_prestamo', views.anadir_prestamo, name='anadir_prestamo'),
  path('borrar_prestamo', views.borrar_prestamo, name='borrar_prestamo'),
  path('modificar_prestamo/<int:id_prestamo>', views.modificar_prestamo, name='modificar_prestamo'),
  path('peliculas', views.peliculas, name='peliculas'),
]
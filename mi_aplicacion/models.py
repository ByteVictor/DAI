# mi_aplicacion/models.py
from django.db import models
from django.utils import timezone


class Autor(models.Model):
    nombre = models.CharField(max_length=100)

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor  = models.ManyToManyField(Autor)
    #portada = models.ImageField(upload_to='Libro')
    
    def __str__(self):
        return self.titulo

class Prestamo(models.Model):
  libro   = models.ForeignKey(Libro, on_delete=models.CASCADE)
  fecha   = models.DateField(default=timezone.now)
  usuario = models.CharField(max_length=100)
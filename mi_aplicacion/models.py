# mi_aplicacion/models.py
from django.db import models
from django.utils import timezone


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    autores  = models.ManyToManyField(Autor)
    portada = models.ImageField(upload_to='static/img/')
    
    def __str__(self):
        return self.titulo

class Prestamo(models.Model):
    id = models.AutoField(primary_key=True)
    libro   = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha   = models.DateField(default=timezone.now)
    usuario = models.CharField(max_length=100)
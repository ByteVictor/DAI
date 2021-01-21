from django.forms import ModelForm
from .models import Autor, Libro, Prestamo

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre']

class LibroForm(ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autores', 'portada']

class PrestamoForm(ModelForm):
    class Meta:
        model = Prestamo
        fields = ['libro', 'fecha', 'usuario']
# mi_aplicacion/views.py

from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseBadRequest
from .forms import *
from .models import Autor, Libro, Prestamo

# Create your views here.

def index(request):
    context = {}
    return render(request,'base.html', context)

def test_template(request):
    context = {}   # Aquí van la las variables para la plantilla
    return render(request,'test.html', context)

def lista_autores(request):
    context = {'autores':Autor.objects.all()}
    return render(request,'listado_autores.html', context)

def anadir_autor(request):
    form = AutorForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():
            nuevo_autor = Autor(nombre=form.cleaned_data.get('nombre'))

            nuevo_autor.save()

            return redirect('/lista_autores')
    else:
        return render(request, 'formulario_crispy.html', {'form': AutorForm})

def borrar_autor(request):
    form = request.POST.dict()

    if request.method == 'POST':
        try:
            autor = Autor.objects.get(id=form.get('autor_id'))
            autor.delete()
        except:
            return HttpResponseBadRequest()

    return redirect('/lista_autores')

def modificar_autor(request, id_autor):
    
    if request.method == 'POST':
        form = request.POST.dict()
        #Si venimos de la lista
        if form.get('autor_id'):
            try:
                autor_modif = Autor.objects.get(id=form.get('autor_id'))

                formulario_modificar = AutorForm(instance=autor_modif)

                return render(request, 'formulario_crispy.html', {'form': formulario_modificar})
            except:
                return HttpResponseBadRequest()
        #si venimos del formulario de modificacion
        else:
            form = AutorForm(request.POST)
            if form.is_valid():
                try:
                    autor_modif = Autor.objects.get(id=id_autor)
                    autor_modif.nombre = form.cleaned_data.get('nombre')
                    autor_modif.save()
                except:
                    return HttpResponseBadRequest()
            else:
                return HttpResponseBadRequest()
            
    return redirect('/lista_autores')

def lista_libros(request):
    context = {'libros':Libro.objects.all()} 
    return render(request,'listado_libros.html', context)

def anadir_libro(request):
    form = LibroForm(request.POST, request.FILES)

    if request.method == 'POST':

        if form.is_valid():

            nuevo_libro = form.save(commit=False)
            autor = form.cleaned_data['autores']
            nuevo_libro.save()

            nuevo_libro.autores.set(autor)


            return redirect('/lista_libros')
        else:
            return HttpResponse('formulario invalido')
    else:
        return render(request, 'formulario_crispy.html', {'form': LibroForm})

def borrar_libro(request):
    form = request.POST.dict()

    if request.method == 'POST':
        if form.get('libro_id') != '':
            libro = Libro.objects.get(id=form.get('libro_id'))
            libro.delete()

    return redirect('/lista_libros')

def modificar_libro(request, id_libro):
       
    if request.method == 'POST':
        form = request.POST.dict()
        #Si venimos de la lista
        if form.get('libro_id'):
            try:
                libro_modif = Libro.objects.get(id=form.get('libro_id'))

                formulario_modificar = LibroForm(instance=libro_modif)

                return render(request, 'formulario_crispy.html', {'form': formulario_modificar})
            except:
                return HttpResponseBadRequest()
        #si venimos del formulario de modificacion
        else:
            try:
                libro_modif = Libro.objects.get(id=id_libro)
            except:
                return HttpResponseBadRequest()

            form = LibroForm(request.POST, request.FILES, instance=libro_modif)
            if form.is_valid():
                libro_modif.titulo = form.cleaned_data.get('titulo')
                libro_modif.portada = form.cleaned_data.get('portada')
                autor = form.cleaned_data['autores']

                libro_modif.save()

                libro_modif.autores.set(autor)
            else:
                return HttpResponse('formulario invalido')
            
    return redirect('/lista_libros')

def lista_prestamos(request):
    context = {'prestamos':Prestamo.objects.all()}
    return render(request,'listado_prestamos.html', context)

def anadir_prestamo(request):
    form = PrestamoForm(request.POST, request.FILES)

    if request.method == 'POST':

        if form.is_valid():
            nuevo_prestamo = form.save(commit=False)
            libro = form.cleaned_data['libro']
            nuevo_prestamo.libro = libro
            nuevo_prestamo.save()

            return redirect('/lista_prestamos')
        else:
            return HttpResponse('formulario invalido')
    else:
        return render(request, 'formulario_crispy.html', {'form': PrestamoForm})

def borrar_prestamo(request):
    form = request.POST.dict()

    if request.method == 'POST':
        if form.get('prestamo_id') != '':
            prest = Prestamo.objects.get(id=form.get('prestamo_id'))
            prest.delete()

    return redirect('/lista_prestamos')

def modificar_prestamo(request, id_prestamo):
       
    if request.method == 'POST':
        form = request.POST.dict()
        #Si venimos de la lista
        if form.get('prestamo_id'):
            try:
                prest_modif = Prestamo.objects.get(id=form.get('prestamo_id'))

                formulario_modificar = PrestamoForm(instance=prest_modif)

                return render(request, 'formulario_crispy.html', {'form': formulario_modificar})
            except:
                return HttpResponseBadRequest()
        #si venimos del formulario de modificacion
        else:
            form = PrestamoForm(request.POST)
            if form.is_valid():
                try:
                    prest_modif = Prestamo.objects.get(id=id_prestamo)
                    prest_modif.libro = form.cleaned_data.get('libro')
                    prest_modif.fecha = form.cleaned_data.get('fecha')
                    prest_modif.usuario = form.cleaned_data.get('usuario')

                    prest_modif.save()

                except:
                    return HttpResponseBadRequest()
            
    return redirect('/lista_prestamos')
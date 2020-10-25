#./app/app.py
from flask import Flask, render_template
from ejercicios.ejercicio2 import ejercicio2
from ejercicios.ejercicio3 import ejercicio3
from ejercicios.ejercicio5 import ejercicio5
from ejercicios.ejercicio6 import ejercicio6

from io import StringIO
import sys

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ordena/<tamano>')
def ordena(tamano):
    #Guardamos la salida por consola en una variable
    salida = StringIO()
    sys.stdout = salida
    ejercicio2(tamano)
    
    return salida.getvalue()

@app.route('/criba/<tamano>')
def criba(tamano):
    #Guardamos la salida por consola en una variable
    salida = StringIO()
    sys.stdout = salida
    ejercicio3(tamano)
    
    return salida.getvalue()

@app.route('/fibonacci/<tamano>')
def fibonacci(tamano):
    return "Ver ficheros leeEJ4 y escribeJ4"
    
@app.route('/cadenas/<cadena>')
def cadenas(cadena):
    #Guardamos la salida por consola en una variable
    salida = StringIO()
    sys.stdout = salida
    ejercicio5(cadena)
    
    return salida.getvalue()

@app.route('/regex')
def reg_ex():
    #Guardamos la salida por consola en una variable
    salida = StringIO()
    sys.stdout = salida
    ejercicio6()
    
    return salida.getvalue()

@app.errorhandler(404)
def page_notfound(error):
    return render_template('notfound.html'), 404
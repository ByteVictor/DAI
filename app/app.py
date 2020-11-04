#./app/app.py
from flask import Flask, render_template, session, request, redirect, url_for
#from ejercicios.ejercicio1 import ejercicio1
from ejercicios.ejercicio2 import ejercicio2
from ejercicios.ejercicio3 import ejercicio3
from ejercicios.ejercicio5 import ejercicio5
from ejercicios.ejercicio6 import ejercicio6

from io import StringIO
import sys
from model import *

app = Flask(__name__)

app.secret_key = 'clavesuperhipermegasecreta'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if( request.method == 'POST' ):
        if( request.form['email'] == db['user']['email']
        and request.form['password'] == db['user_pass']['pass'] ):
            session['email'] = request.form['email']

    if not 'email' in session:
        return render_template('login.html', session=session, intentado=(request.method=='POST'))
    else:
        return redirect(url_for('index'))


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    #Eliminamos el email, por lo tanto estamos deslogeados
    session.pop('email')

    return redirect(url_for('index'))

@app.route('/adivinacion')
def adivinacion():
    return render_template('vistaejercicio.html')

@app.route('/ordena/<tamano>')
def ordena(tamano):
    #Guardamos la salida por consola en una variable
    salida = StringIO()
    sys.stdout = salida
    ejercicio2(tamano)
    
    
    return render_template('vistaejercicio.html', salida=salida.getvalue())

@app.route('/criba/<tamano>')
def criba(tamano):
    #Guardamos la salida por consola en una variable
    salida = StringIO()
    sys.stdout = salida
    ejercicio3(tamano)
    
    return render_template('vistaejercicio.html', salida=salida.getvalue())

@app.route('/fibonacci/<tamano>')
def fibonacci(tamano):
    return render_template('vistaejercicio.html', salida="Ver ficheros leeEJ4 y escribeJ4") 
    
@app.route('/cadenas/<cadena>')
def cadenas(cadena):
    #Guardamos la salida por consola en una variable
    salida = StringIO()
    sys.stdout = salida
    ejercicio5(cadena)
    
    return render_template('vistaejercicio.html', salida=salida.getvalue())

@app.route('/regex')
def reg_ex():
    #Guardamos la salida por consola en una variable
    salida = StringIO()
    sys.stdout = salida
    ejercicio6()
    
    return render_template('vistaejercicio.html', salida=salida.getvalue())

@app.errorhandler(404)
def page_notfound(error):
    return render_template('notfound.html'), 404
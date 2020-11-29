#./app/app.py
from flask import Flask, render_template, session, request, redirect, url_for
from ejercicios.ejercicio1 import ejercicio1
from ejercicios.ejercicio2 import ejercicio2
from ejercicios.ejercicio3 import ejercicio3
from ejercicios.ejercicio5 import ejercicio5
from ejercicios.ejercicio6 import ejercicio6
from ejercicios.ejercicio6 import correo_electronico

from io import StringIO
import sys
import random
from model import *

from pymongo import MongoClient

app = Flask(__name__)

app.secret_key = 'clavesuperhipermegasecreta'

#Mongo:
client = MongoClient("mongo", 27017)
db = client.SampleCollections
##

def anadir_ultimolinkvisitado(link, texto):
		if not 'ultimos_links' in session:
				session['ultimos_links'] = []
		
		if ( len(session['ultimos_links']) < 3):
				session['ultimos_links'].append({ 'link' : link,
																					'texto': texto })
		else:
				session['ultimos_links'].pop(0)
				session['ultimos_links'].append({ 'link' : link,
																					'texto': texto })

		session['tamano_links'] = len(session['ultimos_links'])

@app.route('/')
def index():
		anadir_ultimolinkvisitado('/', 'Inicio')
		return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
		anadir_ultimolinkvisitado('/login', 'Login')

		if( request.method == 'POST' ):
				if( check_user(request.form['email'], request.form['password']) ):
						session['email'] = request.form['email']

		if not 'email' in session:
				return render_template('login.html', intentado=(request.method=='POST'))
		else:
				return redirect(url_for('index'))

@app.route('/logout', methods=['GET', 'POST'])
def logout():
		#Eliminamos el email, por lo tanto estamos deslogeados
		session.pop('email')

		return redirect(url_for('index'))

@app.route('/register', methods=['GET','POST'])
def registro():
		anadir_ultimolinkvisitado('/register', 'Registro')
		resultado_registro = True
		datosCorrectos = request.method =='GET'

		if not 'email' in session:
				if( request.method == 'POST' ):
						if( correo_electronico(request.form['email']) 
								and request.form['password'] ):
								datosCorrectos = True
								resultado_registro = registrar(request.form['email'], request.form['password'])

				if ( request.method =='GET' or not datosCorrectos or not resultado_registro):
						return render_template('registro.html', validos=datosCorrectos, res = resultado_registro)
				else:
						return redirect(url_for('index'))
		else:
				return redirect(url_for('index'))

@app.route('/mongo', methods=['GET','POST'])
def mongo():
    anadir_ultimolinkvisitado('/', 'Lista (mongo)')
    pelis = db.Sakila_films.find()

    if( request.method == 'POST' ):
	    lista_pelis = []

	    for peli in pelis:
	        app.logger.debug(pelis) # salida consola
	        lista_pelis.append(peli)
	    
		return render_template('lista.html', lista_pelis=lista_pelis)
	else:
		return render_template('lista.html')


@app.route('/adivinacion', methods=['GET','POST'])
def adivinacion():
		anadir_ultimolinkvisitado('/adivinacion', 'Ejercicio 1 (Adivinación)')
		salida = StringIO()
		sys.stdout = salida

		cuerpo = { 'titulo'        : 'Adivinación',
							 'resumen'       : 'Intenta adivinar el número correcto',
							 'mensaje_error' : 'El valor introducido no es válido'}

		if not 'numero_aleatorio' in session or not 'numero_intentos' in session: 
				session['numero_aleatorio'] = random.randint(1, 100)
				session['numero_intentos'] = 10
				print('Reasignando numero', file=sys.stderr)

		if( request.method=='POST' and 'intento' in request.form ):
				enviado = 'error'
				if( request.form['intento'].isnumeric() ):
						intento = int(request.form['intento'])
						enviado = 'correcto'

						res = ejercicio1(intento, session['numero_aleatorio'])

						if( session['numero_intentos'] <= 1 ):
								session['numero_aleatorio'] = random.randint(1, 100)
								session['numero_intentos'] = 10
								print('Ultimo intento fallido, reasignando', file=sys.stderr)
						else:
								session['numero_intentos'] -= 1

						cuerpo['resumen'] += ', te quedan <b>' + str(session['numero_intentos']) + ' intentos </b> '


						print(session['numero_aleatorio'], file=sys.stderr)

						if( res ):
								cuerpo['resumen'] = 'Felicidades! lo adivinaste, puedes volver a jugar'
								session.pop('numero_aleatorio')
								print('Reiniciando numero_aleatorio', file=sys.stderr)

				return render_template('vistaejercicio.html'
															, cuerpo  = cuerpo
															, salida  = salida.getvalue()
															, enviado = enviado)
		else:
				return render_template('vistaejercicio.html'
															, cuerpo  = cuerpo
															, salida  = salida.getvalue()
															, enviado = False)

@app.route('/ordena', methods=['GET','POST'])
def ordena():
		anadir_ultimolinkvisitado('/ordena', 'Ejercicio 2 (Ordenación)')
		#Guardamos la salida por consola en una variable
		salida = StringIO()
		sys.stdout = salida
	 
		cuerpo = { 'titulo'        : 'Ordenación',
							 'resumen'       : 'Introduce el tamaño del array a ordenar',
							 'mensaje_error' : 'El valor introducido no es válido'}
		

		if( request.method=='POST' and 'intento' in request.form ):
				enviado = 'error'
				if( request.form['intento'].isnumeric() ):
						intento = int(request.form['intento'])
						enviado = 'correcto'
						ejercicio2(intento)

				return render_template('vistaejercicio.html'
															, cuerpo = cuerpo
															, salida  = salida.getvalue()
															, enviado = enviado)
		else:
				return render_template('vistaejercicio.html'
															, cuerpo = cuerpo)
		

@app.route('/criba', methods=['GET','POST'])
def criba():
		anadir_ultimolinkvisitado('/criba', 'Ejercicio 3 (Criba)')
		#Guardamos la salida por consola en una variable
		salida = StringIO()
		sys.stdout = salida
		
		cuerpo = { 'titulo'        : 'Criba',
							 'resumen'       : 'Introduce el tamaño de la criba',
							 'mensaje_error' : 'El valor introducido no es válido'}
		

		if( request.method=='POST' and 'intento' in request.form ):
				enviado = 'error'
				if( request.form['intento'].isnumeric() ):
						intento = int(request.form['intento'])
						enviado = 'correcto'
						ejercicio3(intento)

				return render_template('vistaejercicio.html'
															, cuerpo = cuerpo
															, salida  = salida.getvalue()
															, enviado = enviado)
		else:
				return render_template('vistaejercicio.html'
															, cuerpo = cuerpo)

@app.route('/fibonacci', methods=['GET','POST'])
def fibonacci():
		anadir_ultimolinkvisitado('/fibonacci', 'Ejercicio 4 (Fibonacci)')

		cuerpo = { 'titulo'        : 'Fibonacci',
							 'resumen'       : 'Introduce el tamaño de la criba',
							 'noformulario'  : True}
		return render_template('vistaejercicio.html'
													, salida="Ver ficheros leeEJ4 y escribeJ4"
													, cuerpo=cuerpo
													, enviado='correcto') 
		
@app.route('/cadenas', methods=['GET','POST'])
def cadenas():
		anadir_ultimolinkvisitado('/cadenas', 'Ejercicio 5 (Cadenas)')
		#Guardamos la salida por consola en una variable
		salida = StringIO()
		sys.stdout = salida
		
		cuerpo = { 'titulo'        : 'Analizador de Cadenas',
							 'resumen'       : 'Introduce la cadena a analizar',
							 'mensaje_error' : 'La cadena introducida no es válida'}
		

		if( request.method=='POST' and 'intento' in request.form ):
				enviado = 'correcto'

				intento = request.form['intento']
				
				ejercicio5(intento)

				return render_template('vistaejercicio.html'
															, cuerpo = cuerpo
															, salida  = salida.getvalue()
															, enviado = enviado)
		else:
				return render_template('vistaejercicio.html'
															, cuerpo = cuerpo)

@app.route('/regex', methods=['GET','POST'])
def reg_ex():
		anadir_ultimolinkvisitado('/regex', 'Ejercicio 6 (Analisis expresiones regulares)')
		#Guardamos la salida por consola en una variable
		salida = StringIO()
		sys.stdout = salida
		
		cuerpo = { 'titulo'        : 'Análisis de expresiones regulares',
							 'resumen'       : 'Introduce una cadena para ser evaluada',
							 'mensaje_error' : 'La cadena introducida no es válida'}
		

		if( request.method=='POST' and 'intento' in request.form ):
				enviado = 'correcto'

				intento = request.form['intento']
				
				ejercicio6(intento)

				return render_template('vistaejercicio.html'
															, cuerpo = cuerpo
															, salida  = salida.getvalue()
															, enviado = enviado)
		else:
				return render_template('vistaejercicio.html'
															, cuerpo = cuerpo)

@app.errorhandler(404)
def page_notfound(error):
		return render_template('notfound.html'), 404
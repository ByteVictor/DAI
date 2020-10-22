import random
import time

def medir_tiempo(funcion, matriz):
    tic = time.perf_counter()
    funcion(matriz)
    toc = time.perf_counter()
    
    tiempo = toc - tic
    
    print(f'Ha tardado: {tiempo:0.20f} segundos')
    return tiempo

def ordenacion_seleccion(matriz):
    for i in range(0, len(matriz)):
        minimo = matriz[i]
        pos_minimo = i

        for j in range(i+1, len(matriz)):
            if( matriz[j] < minimo):
                minimo = matriz[j]
                pos_minimo = j

        swap = matriz[i]
        matriz[i] = matriz[pos_minimo]
        matriz[pos_minimo] = swap

    
    print("Matriz ordenada por seleccion:\n", matriz)

def ordenacion_insercion(matriz):
    for i in range(1, len(matriz)):
        insert = matriz[i]

        j = i
        while(j > 0 and insert < matriz[j-1] ):
            matriz[j] = matriz[j-1]
            j -= 1

        matriz[j] = insert

    print("Matriz ordenada por insercion:\n", matriz)

def ordenacion_burbuja(matriz):
    for i in range(0, len(matriz)):
        for j in range(len(matriz)-1, i, -1):
            if(matriz[j] < matriz[j-1]):
                swap = matriz[j]
                matriz[j] = matriz[j-1]
                matriz[j-1] = swap

    print("Matriz ordenada por burbuja:\n", matriz)

matriz = []

print("Introduce el tamaño de la matriz: ")
tamano_matriz = int(input())

for i in range(0, tamano_matriz):
    matriz.append(random.randint(1, 100))

print("Matriz inicial:\n", matriz)

tiempo_seleccion  = medir_tiempo(ordenacion_seleccion, matriz[:])
tiempo_insercion = medir_tiempo(ordenacion_insercion, matriz[:])
tiempo_burbuja    = medir_tiempo(ordenacion_burbuja  , matriz[:])

if( tiempo_seleccion < tiempo_insercion and tiempo_seleccion < tiempo_burbuja):
    print(f'La ordenacion por seleccion ha sido la mas rapida: {tiempo_seleccion:0.20f}')
elif(tiempo_insercion < tiempo_seleccion and tiempo_insercion < tiempo_burbuja):
    print(f'La ordenacion por insercion ha sido la mas rapida: {tiempo_insercion:0.20f}')
else:
    print(f'La ordenacion por burbuja ha sido la mas rapida: {tiempo_burbuja:0.20f}')


#A partir de un numero lo suficientemente grande de datos, gana siempre la ordenacion por seleccion
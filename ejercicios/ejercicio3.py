
import math

def criba_erastotenes(numero):
    lista_numeros = []

    #Metemos el dos ya que es el unico par que es primo
    lista_numeros.append(2)

    #Metemos todos los numeros impares hasta raiz de n
    for i in range(3, numero, 2):
         lista_numeros.append(i)
    
    i = 0
    #Para cada numero de la lista
    while( i < len(lista_numeros)):
        #Para el resto de numeros de la lista
        j = i + 1
        while( j < len(lista_numeros)):
            #Comprobamos si es multiplo
            if( lista_numeros[j] % lista_numeros[i] == 0):
                #Si es multiplo lo sacamos de la lista
                lista_numeros.pop(j)
            else:
                j += 1
        i += 1


    if not lista_numeros:
        return -1
    else:
        return lista_numeros


print("Se cribaran todos los numeros naturales desde 2 hasta: ")
n = int(input())

resultado = criba_erastotenes(n)
print( resultado )

print( "Hay un total de ", len(resultado), " primos anteriores a ", n)
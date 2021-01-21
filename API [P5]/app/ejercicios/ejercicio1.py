
def ejercicio1(intento_adivinacion, numero_aleatorio = 0):
        
    if intento_adivinacion != numero_aleatorio:
        if(intento_adivinacion > numero_aleatorio):
            print("El número es menor")
        if(intento_adivinacion < numero_aleatorio):
            print("El número es mayor")
    else:
        print("Correcto!")
        return True

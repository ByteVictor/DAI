import random

print("Adivina el número")


numero_aleatorio = random.randint(1, 100)

intento_adivinacion = None

while intento_adivinacion != numero_aleatorio:
    print("Introduce un número: ")
    intento_adivinacion = int(input())

    if(intento_adivinacion > numero_aleatorio):
        print("El número es menor")
    if(intento_adivinacion < numero_aleatorio):
        print("El número es mayor")

print("Correcto!")

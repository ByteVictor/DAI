
def calcularFibonacci(n):
    numeros_fibo = [0, 1]

    if(n <= 1):
        return 0

    n -= 2

    for i in range(n):
        suma = numeros_fibo[0] + numeros_fibo[1]
        numeros_fibo[0] = numeros_fibo[1]
        numeros_fibo[1] = suma

    return numeros_fibo[1]




lf = open("./ejercicios/leeEJ4.txt", "r")
ef = open("./ejercicios/escribeEJ4.txt", "w")

n = lf.read()

print("Leido: ", n)
print("Calculando... ", end='')

n = int(n)
for i in range(1, n+1):
    print( calcularFibonacci(i) , end=' ')
print('\n')

ef.write( str(calcularFibonacci( n )) )


def cadena_balanceada(cadena):
    balance = 0

    for i in range(len(cadena)):
        if(cadena[i] == '['):
            balance += 1
        elif(cadena[i] == ']'):
            balance -= 1

        if(balance < 0):
            return False
    
    return balance == 0
            
def test(cond):
    if(cond):
        return "✓" 
    else:
        return "✘"

cadena1 = "[][][][][]]["
cadena2 = "[]][x[[]][][]"
cadena3 = "[[]][[[x]]]"

print(test(cadena_balanceada(cadena1)), cadena1)
print(test(cadena_balanceada(cadena2)), cadena2)
print(test(cadena_balanceada(cadena3)), cadena3)


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

def ejercicio5(cadena):
    cadena1 = "[][][][][]]["
    cadena2 = "[]][x[[]][][]"
    cadena3 = "[[]][[[x]]]"

    print("Tests <br>")
    print(test(cadena_balanceada(cadena1)), cadena1, "<br>")
    print(test(cadena_balanceada(cadena2)), cadena2, "<br>")
    print(test(cadena_balanceada(cadena3)), cadena3, "<br>")

    print("<br><br>Cadena para testear: ", cadena, test(cadena_balanceada(cadena)) )

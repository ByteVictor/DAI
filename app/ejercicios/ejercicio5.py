
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
        return "<div class='alert alert-success'>Correcto ✓</div>" 
    else:
        return "<div class='alert alert-danger'>Incorrecto ✘</div>"

def ejercicio5(cadena):
    cadena1 = "[][][][][]]["
    cadena2 = "[]][x[[]][][]"
    cadena3 = "[[]][[[x]]]"

    print("<b>EJEMPLOS:</b> <br>")
    print(cadena1, test(cadena_balanceada(cadena1)),  "<br>")
    print(cadena2, test(cadena_balanceada(cadena2)),  "<br>")
    print(cadena3, test(cadena_balanceada(cadena3)),  "<br>")

    print("<br><br>Cadena para testear: ", cadena, test(cadena_balanceada(cadena)) )

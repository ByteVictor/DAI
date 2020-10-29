import re



def palabra_espacio_mayus(cadena):
    reg_ex = "\w*\s[A-Z]"

    res = re.search(reg_ex, cadena)

    return res != None

def correo_electronico(cadena):
    reg_ex = "[_a-zA-Z0-9-]+([_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+([a-zA-Z0-9-]+)*(\.[a-z]{2,4})"

    res = re.search(reg_ex, cadena)

    return res != None

def numero_credito(cadena):
    reg_ex = "(\d{4}\s\d{4}\s\d{4}\s\d{4}(\s|$))|(\d{4}-\d{4}-\d{4}-\d{4}(\s|$))"

    res = re.search(reg_ex, cadena)

    return res != None


def ejercicio6():
    test_palabra_malo = "Palabra "
    test_palabra_bueno = "Palabra N"
    print(test_palabra_malo, palabra_espacio_mayus(test_palabra_malo), "<br>")
    print(test_palabra_bueno, palabra_espacio_mayus(test_palabra_bueno), "<br>")

    test_correo_malo = "correo@sadas"
    test_correo_bueno = "correo@correo.es"
    print(test_correo_malo, correo_electronico(test_correo_malo), "<br>")
    print(test_correo_bueno, correo_electronico(test_correo_bueno), "<br>")

    test_numero_malo = "4832-3478 8474-4833"
    test_numero_bueno = "3439 3494 3949 3939"
    test_numero_bueno2 = "3494-3232-3213-3213"
    print(test_numero_malo, numero_credito(test_numero_malo), "<br>")
    print(test_numero_bueno, numero_credito(test_numero_bueno), "<br>")
    print(test_numero_bueno2, numero_credito(test_numero_bueno2), "<br>")

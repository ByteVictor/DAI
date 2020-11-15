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

def test(cond):
    if(cond):
        return "<div class='alert alert-success'>Correcto ✓</div>" 
    else:
        return "<div class='alert alert-danger'>Incorrecto ✘</div>"


def ejercicio6(cadena):
    print("<b>EJEMPLOS:</b> <br>")
    print("<b>Una palabra un espacio y una mayúscula:</b><br>")
    test_palabra_malo = "Palabra "
    test_palabra_bueno = "Palabra N"
    print(test_palabra_malo, palabra_espacio_mayus(test_palabra_malo), "<br>")
    print(test_palabra_bueno, palabra_espacio_mayus(test_palabra_bueno), "<br>")

    print("<b>Un correo</b><br>")
    test_correo_malo = "correo@sadas"
    test_correo_bueno = "correo@correo.es"
    print(test_correo_malo, correo_electronico(test_correo_malo), "<br>")
    print(test_correo_bueno, correo_electronico(test_correo_bueno), "<br>")

    print("<b>Un código de 4 grupos de 4 números separados por espacios o guiones</b><br>")
    test_numero_malo = "4832-3478 8474-4833"
    test_numero_bueno = "3439 3494 3949 3939"
    test_numero_bueno2 = "3494-3232-3213-3213"
    print(test_numero_malo, numero_credito(test_numero_malo), "<br>")
    print(test_numero_bueno, numero_credito(test_numero_bueno), "<br>")
    print(test_numero_bueno2, numero_credito(test_numero_bueno2), "<br>")

    print("<br><b>Cadena:</b>")
    print("<br><input class=\"form-control\" type=\"text\" placeholder=\"",cadena,"\" readonly><br>")

    print("<b>Palabra-Espacio-Mayus</b>", test(palabra_espacio_mayus(cadena)))
    print("<b>Correo</b>", test(correo_electronico(cadena)))
    print("<b>Código</b>", test(numero_credito(cadena)))


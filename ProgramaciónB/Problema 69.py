# Problema 69. Verificación correo electrónico

def verificacion(email):
    if "@" in email:
        verif = print("Tu dirección de correo electrónico es válida")
    else:
        verif = print("Tu dirección de correo electrónico es inválida")
    return verif

email = input("Introduce tu dirección de email: ")
verificacion(email)

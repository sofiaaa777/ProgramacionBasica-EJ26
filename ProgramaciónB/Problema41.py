# Problema 41. Confirmación de contraseña (sin límite)

cont = input("Introduzca una contraseña: ")
cont2 = None
while cont2 == None or cont2 != cont:
    cont2 = input("Introduzca de nuevo su contraseña: ")

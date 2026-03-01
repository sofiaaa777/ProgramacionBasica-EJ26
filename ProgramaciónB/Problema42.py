# Problema 42. Confirmación de contraseña (con líminte)

cont = input("Introduce una contraseña: ")
i = 3
while i > 0:
    if input("Introduce de nuevo tu contraseña: ") != cont:
        i = i - 1
    else:
        print("Contraseña correcta")
else:
    print("Cuenta Cancelada")
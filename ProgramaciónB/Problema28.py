# Problema 28. Mayoría de edad.

edad = int(input("Introduce tu edad: "))
if edad < 0:
    print("Opción invalida")
elif edad >= 18:
    print("Eres mayor de edad")
else: print("Eres menor de edad")
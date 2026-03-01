# Problema 27. Área o perímetro de un cuadrado.

print("¿Qué quieres calcular?, "
          "1. El area de un cuadrado "
          "2. El perímetro de un cuadrado: ")
opc = int(input())
if opc > 2 or opc < 1: print("Opción inválida")
lado = int(input("Lado del cuadrado: "))
if lado < 0:
    print("Los lados del cuadrado deben ser positivos")
elif opc == 1:
    A = lado * lado
    print ("EL área del cuadrado es: ", A)
elif opc == 2:
    P = 4 * lado
    print("El perímetro del cuadrado es: ", P)
else: print("La primera opción es invalida")

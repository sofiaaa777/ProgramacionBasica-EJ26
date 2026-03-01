# Problema 36. Repetir elevación al cuadrado

op = 0
while op == 0 or op == 1:
    num = float(input("Introduce un número cualquiera: "))
    num2 = num * num
    print("El número al cuadrado es:", num2)
    num = None
    op = int(input("¿Quieres ingresar otro número? (1. Si / 2. No) "))
    while op > 2 or op < 1:
        op = None
        op = int(input("¿Quieres ingresar otro número? (1. Si / 2. No) "))
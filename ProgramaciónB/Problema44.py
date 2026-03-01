# Problema 44. Calculadora básica con repetición.

opción = 0
while opción == 0 or opción == 1:
    opción = 0
    num1 = float(input("De un número cualquiera: "))
    num2 = float(input("De un número cualquiera: "))
    operación = input("Elija un operador (+, -, *, /, **, %): ")
    if operación == "+":
        result = num1 + num2
    elif operación == "-":
        result = num1 - num2
    elif operación == "*":
        result = num1 * num2
    elif operación == "/":
        result = num1 / num2
    elif operación == "**":
        result = num1 ** num2
    elif operación == "%":
        result = num1 % num2
    else:
        print("Operador inválido")
    print("resultado = ", result)
    while opción == None or opción < 1 or opción > 2:
        opción = None
        opción = int(input("¿Desea realizar otra operación? (1. Si / 2. No): "))
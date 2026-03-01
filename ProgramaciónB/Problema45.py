# Problema 45. Calculadora con repetición por operación.

continuar = True

while continuar:
    num1 = float(input("De un número cualquiera: "))
    num2 = float(input("De un número cualquiera: "))
    operación = input("Elija un operador (+, -, *, /, **, %): ")
    repetir = True
    while repetir:
        operador_val = True
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
            operador_val = False
        if operador_val:
            print("Resultado = ", result)
            op_repetir = int(input("¿Desea repetir la misma operación? (1. Si / 2. No): "))
            if op_repetir == 2:
                repetir = False
        else:
            repetir = False

    op_continuar = int(input("¿Desea realizar una operación diferente? (1. Si / 2. No): "))
    if op_continuar != 1:
        continuar = False
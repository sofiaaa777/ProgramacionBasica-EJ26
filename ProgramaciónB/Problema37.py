# Problema 37. Interés compuesto con repetición

op = 0
while op == 1 or op == 0:
    C, i, n, M =None, None, None, None
    C = float(input("Introduzca su capital inicial: $"))
    i = float(input("Introduzca la taza de interés: %"))
    n = int(input("Introduzca el número de periodos: "))
    i = i * 0.01
    M = C * ( 1 + i ) ** n
    print("Monto total: $", M)
    op = int(input("¿Desea  hacer otro cálculo? (1. Si / 2. No) "))
    while op < 1 or op > 2:
        op = None
        op = int(input("¿Desea  hacer otro cálculo? (1. Si / 2. No) "))
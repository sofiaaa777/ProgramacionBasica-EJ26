# Problema 43. Acumulador de abonos.

abono = None
abonotot = 0
i = None
while i != 1:
    abono = float(input("¿Cantidad a abonar? $"))
    while abono < 0:
        print("Error")
        abono = None
        abono = float(input("¿Cantidad a abonar? $"))
    abonotot = abonotot + abono
    if abonotot > 100000:
            i = 1
            print("Abono total: $", abonotot)

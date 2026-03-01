# Problema 29. División segura.


div2 = int(input("Introduce un dividendo: "))
div1 = int(input("Introduce un divisor: "))
if div1 == 0:
    print("Opción invalida")
else:
    division = div2 / div1
    print(div2, " / ",div1, " = ", division)
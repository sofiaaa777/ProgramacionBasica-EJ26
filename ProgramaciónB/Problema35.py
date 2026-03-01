# Problema 35. Orden descendente de tres números.

num1 = int(input("Introduce un número cualquiera: "))
num2 = int(input("Introduce un número cualquiera: "))
num3 = int(input("Introduce un número cualquiera: "))
if num1 >= num2 and num1 >= num3:
    if num2 >= num3: print(num1, num2, num3)
    else: print(num1, num3, num2)
if num2 > num1 and num2 > num3:
    if num1 >= num3: print(num2, num1, num3)
    else: print(num2, num3, num1)
if num3 > num1 and num3 >= num2:
    if num2 >= num1: print(num3, num2, num1)
    else: print(num3, num1, num2)
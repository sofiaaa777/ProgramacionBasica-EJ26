# Problema 64. Multiplos.

def EsMultiplo(num1, num2):
    if num1 % num2 == 0:
        return print("Si es multiplo")
    if num1 % num2 != 0:
        return print("No es multiplo")

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

multiplo = EsMultiplo(num1, num2)

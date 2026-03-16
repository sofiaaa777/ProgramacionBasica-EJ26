# Problema 65. Factorial de cada número.

import math

numeros = []
cantidad = 0

def factorial(numeros):
    factoriales = []
    for i in range(len(numeros)):
        fact = math.factorial(numeros[i])
        factoriales.append(fact)
    return factoriales

while True:
    num = input("Introduce un número (escribe 'no' para cancelar): ")
    num = num.lower()
    if num == "no":
        break
    else:
        try:
            num = int(num)
            n = num
            numeros.append(n)
            cantidad = cantidad + 1
        except ValueError:
            print("Valor inválido")

factoriales = factorial(numeros)
print("Factorial de cada número: ", factoriales)
print("Cantidad de números leídos: ", cantidad)

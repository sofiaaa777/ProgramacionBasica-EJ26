# Problema 68. Número primo.

import math

def NumPrimo(num):
    if num % 2 == 1:
        raiz = math.sqrt(num)
        raiz = int(raiz)
        for i in range(2, raiz + 1):
            if num % i == 0:
                indicador = 1
                break
            else:
                indicador = 0
    else:
        indicador = 1
    if indicador == 0:
        resultado = print(num, " es primo")
    else:
        resultado = print(num, " no es primo")
    return resultado

num = int(input("Introduce un número cualquiera: "))
final = NumPrimo(num)
            

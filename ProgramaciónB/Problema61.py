# Problema 61. Perimetro de un rectángulo.

def perimetro(base, altura):
    return base * altura

base = int(input("Introduce la base del rectángulo: "))
altura = int(input("Introduce la altura del rectángulo: "))

print("Perimetro del rectángulo", perimetro(base, altura))

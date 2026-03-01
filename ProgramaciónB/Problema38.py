# Problema 38. Validación de número entre 1 y 5

num = None
while num == None or num < 1 or num > 5:
    num = int(input("Introduce un número entero entre 1 y 5: "))
print("Tu número está en el rango.")
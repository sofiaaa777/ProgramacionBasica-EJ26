# Problema 46. Crear un programa que reciba 10 datos y los muestre elevados al cuadrado.

num_cua = []
for i in range(10):
    num=int(input("Ingrese un número cualquiera: "))
    num2 = num ** 2
    num_cua.append(num2)
print ("Datos elevados al cuadrado:", num_cua)

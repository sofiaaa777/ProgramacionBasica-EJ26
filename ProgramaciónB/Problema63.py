# Problema 63. Cuadrados.

lista = []

while True:
    num = input("Añade un valor a la lista (escribe 'no' para cancelar): ")
    num = num.lower()
    if num == "no":
        break
    else:
        try:
            num  = int(num)
            lista.append(num)
        except ValueError:
            print("Valor inválido")

def lista_cuadrados(lista):
    cuadrados = []
    for i in range(len(lista)):
        cuadrado = lista[i] ** 2
        cuadrados.append(cuadrado)
    return cuadrados

cuadrados = lista_cuadrados(lista)
print("Lista de números al cuadrado: ", cuadrados)

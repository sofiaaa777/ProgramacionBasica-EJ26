# Problema 59. Sumatoria.

lista = []
def numeros():
    num = int(input("Introduzca un número: "))
    lista.append(num)

while True:
    opcion = input("¿Desea añadir un valor a la lista? (Si /No): ")
    opcion = opcion.lower()
    if opcion == "si":
        numeros()
    elif opcion == "no":
        break
    else:
        print("Opción invalida")

suma = 0
def sumatoria(suma):
    for i in range(len(lista)):
        suma = suma + lista[i]
    return suma

suma = sumatoria(suma)
print("Lista de números: ", lista)
print ("Sumatoria: ", suma)

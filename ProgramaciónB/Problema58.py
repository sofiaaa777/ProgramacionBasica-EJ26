# Problema  58. Lista de números.

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

print("Lista de números:", lista)

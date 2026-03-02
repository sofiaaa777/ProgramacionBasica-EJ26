# Problema 53. Lista de 'n' datos.

lista = []
while True:
    dato = input("Introduce un dato (escribe 'no' para cancelar): ")
    if dato.lower() == "no":
        break
    else:
        lista.append(dato)
datosorden = sorted(lista)
print(datosorden)
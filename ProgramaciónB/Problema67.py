# Problema 67. Listas ordenadas.

def ordena_creciente(lista):
    nueva = lista.copy()
    nueva.sort()
    return nueva

def ordena_decreciente(lista):
    nueva = lista.copy()
    nueva.sort(reverse=True)
    return nueva


def elimina_indice(lista, indice):
    nueva = lista.copy()
    eliminado = nueva.pop(indice)
    return eliminado

def elimina_dato(lista, dato):
    nueva = lista.copy()
    nueva.remove(dato)
    return nueva

def estadisticas(lista):
    promedio = sum(lista) / len(lista)
    maximo = max(lista)
    minimo = min(lista)
    return promedio, maximo, minimo

numeros = []

while True:
    print("\n1. Llenar la lista")
    print("2. Ordenar creciente")
    print("3. Ordenar decreciente")
    print("4. Eliminar por índice")
    print("5. Eliminar por dato")
    print("6. Promedio, máximo y mínimo")
    print("7. Mostrar lista")
    print("8. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        while True:
            n = input("Introduce un número (escribe 'no' para cancelar): ")
            if n.lower() == "no":
                break
            else:
                try:
                    n = float(n)
                    numeros.append(n)
                except ValueError:
                    print("Opción inválida")

    elif opcion == "2":
        print("Lista ordenada creciente:", ordena_creciente(numeros))

    elif opcion == "3":
        print("Lista ordenada decreciente:", ordena_decreciente(numeros))

    elif opcion == "4":
        i = int(input("Introduce el índice a eliminar: "))
        print("Elemento eliminado:", elimina_indice(numeros, i))

    elif opcion == "5":
        d = float(input("Introduce el dato a eliminar: "))
        print("Nueva lista:", elimina_dato(numeros, d))

    elif opcion == "6":
        prom, maximo, minimo = estadisticas(numeros)
        print("Promedio:", prom)
        print("Máximo:", maximo)
        print("Mínimo:", minimo)

    elif opcion == "7":
        print("Lista actual:", numeros)

    elif opcion == "8":
        break
    else:
        print("Opción inválida")

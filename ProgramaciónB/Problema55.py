# Problema 55. Lista númerica o de texto.

lista = []

print("¿Qué tipo de lista deseas crear?")
print("1. Números")
print("2. Texto")

tipo = int(input("Opción: "))

numerica = tipo == 1

while True:
    print("MENÚ")
    print("1. Agregar valor")
    print("2. Eliminar valor")
    print("3. Ordenar lista (modificando original)")
    print("4. Ordenar lista (crear nueva)")
    print("5. Buscar elemento")

    if numerica:
        print("6. Estadísticas (max, min, suma, promedio)")
    print("0. Salír")
    op = int(input("Elige opción: "))

    if op == 1:
        valor = input("Valor a agregar: ")
        if numerica:
            valor = float(valor)
        lista.append(valor)
        print("Agregado ✔")

    elif op == 2:
        print("1. Eliminar por índice")
        print("2. Eliminar por valor")
        sub = int(input("Opción: "))

        if sub == 1:
            i = int(input("Índice: "))
            if 0 <= i < len(lista):
                lista.pop(i)
                print("Eliminado")
            else:
                print("Índice inválido")

        elif sub == 2:
            val = input("Valor a eliminar: ")
            if numerica:
                val = float(val)
            if val in lista:
                lista.remove(val)
                print("Eliminado")
            else:
                print("No existe")

    elif op == 3:
        lista.sort()
        print("Lista ordenada")

    elif op == 4:
        nueva = sorted(lista)
        print("Lista ordenada nueva:")
        print(nueva)

    elif op == 5:
        buscar = input("Elemento a buscar: ")
        if numerica:
            buscar = float(buscar)

        indices = []

        for i in range(len(lista)):
            if lista[i] == buscar:
                indices.append(i)

        if indices:
            print("Encontrado en índice(s):", indices)
        else:
            print("No encontrado")

    elif op == 6 and numerica:
        if lista:
            print("Máximo:", max(lista))
            print("Mínimo:", min(lista))
            print("Suma:", sum(lista))
            print("Promedio:", sum(lista) / len(lista))
        else:
            print("Lista vacía")

    elif op == 0:
        print("Programa terminado")
        break

    else:
        print("Opción inválida")

    print("\nLista actual:", lista)
 # Problema 48. Lista de productos

producto = []
claves  = []
piezas = []
while True:
    print ("Menú de opciones \n1. Añadir producto. \n2. Buscar producto.")
    op = int(input("Opción: "))
    if op == 1:
        prod = input("Agrega un producto: ")
        clv = int(input("Clave del producto: "))
        pzs = int(input("Introduce la cantidad de piezas en existencia: "))
        producto.append(prod)
        claves.append(clv)
        piezas.append(pzs)
    elif op == 2:
        i = int(input("Introduce el índice del producto que quiere buscar: "))
        if 0 <= i < len(producto):
            print ("Producto: ", producto[i])
            print ("Clave: ", claves[i])
            print ("Piezas en existencia: ", piezas[i])
            break
        else:
            print("Índice inválido")
    else:
        print("Opción inválida")
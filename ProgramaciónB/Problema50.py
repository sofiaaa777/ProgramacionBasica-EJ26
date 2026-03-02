 # Problema 49. Lista de productos con diccionario

producto = []
claves  = []
piezas = []
datos = {}
while True:
    print ("Menú de opciones \n1. Añadir producto. \n2. Buscar producto. \n3. Mostrar todos los productos. \n4. Salir")
    op = int(input("Opción: "))
    if op == 1:
        prod = input("Agrega un producto: ")
        clv = int(input("Clave del producto: "))
        pzs = int(input("Introduce la cantidad de piezas en existencia: "))
        producto.append(prod)
        claves.append(clv)
        piezas.append(pzs)
    elif op == 2:
        print("Introduce como quieres buscar el producto \n1. Índice \n 2. Nombre \n3. Clave")
        i = int(input("Opción: "))
        if i == 1:
            indice = int(input("Índice: "))
            if 0 <= indice < len(producto):
                print("Producto: ", producto[indice])
                print("Clave: ", claves[indice])
                print("Piezas en existencia: ", piezas[indice])
            else:
                print("Índice inválido")
        elif i == 2:
            nom = input("Introduce el nombre del producto: ")
            if nom in producto:
                k = producto.index(nom)
                print("Producto: ", producto[k])
                print("Clave: ", claves[k])
                print("Piezas en existencia: ", piezas[k])
            else:
                print("Producto no encontrado")
        elif i == 3:
            clave = int(input("Introduce la clave del producto: "))
            if clave in claves:
                k = claves.index(clave)
                print("Producto: ", producto[k])
                print("Clave: ", claves[k])
                print("Piezas en existencia: ", piezas[k])
            else:
                print("Clave no encontrada")
        else:
            print("Opción inválida")
    elif op == 3:
        for j in range(len(producto)):
            datos[producto[j]] = {
                "Clave": claves[j],
                "Piezas en existencia": piezas[j]
            }
        print("Productos disponibles")
        for producto, info in datos.items():
            print(f"Producto: {producto}")
            print(f"Clave: {info['Clave']}")
            print(f"Piezas existentes: {info['Piezas en existencia']}")
    if op == 4:
        print("Saliendo del programa")
        break
    else:
        print("Opción inválida")
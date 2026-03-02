 # Problema 49. Lista de productos con diccionario

producto = []
claves  = []
piezas = []
datos = {}
while True:
    print ("Menú de opciones \n1. Añadir producto. \n2. Buscar producto. \n3. Mostrar todos los productos")
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
        break
    else:
        print("Opción inválida")
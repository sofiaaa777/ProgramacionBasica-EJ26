# Problema 52. 5 productos.

productos = []
precios = []
ventasprod = []

for i in range(5):
    nom = input("Producto: ")
    precio = float(input("Precio del producto: $"))
    ventas = int(input("Total de ventas del producto: "))
    productos.append(nom)
    precios.append(precio)
    ventasprod.append(ventas)
for j in range(len(productos)):
    print(f"Producto: {productos[j]} ${precios[j]}, {ventasprod[j]} ventas totales")
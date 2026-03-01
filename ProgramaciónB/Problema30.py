# Problema 30. Análisis de beneficios

precio = float(input("Precio unitario del producto: $"))
cantven = int(input("Cantidad vendida: "))
egr = float(input("Total de egresos de la empresa: $"))
ing = precio * cantven
if egr > ing:
    per = egr - ing
    print("La empresa está en pérdidas: ", per)
elif ing == egr:
    print("La empresa está en equilibrio: ", ing, " = ", egr)
else:
    gan = ing - egr
    print("La empresa está generando ganancias: ", gan)
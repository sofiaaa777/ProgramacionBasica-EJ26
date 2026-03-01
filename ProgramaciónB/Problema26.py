# Problema 26. Comparar dos números

v1 = int(input("Escribe un número entero cualquiera: "))
v2 = int(input("Escribe un número entero cualquiera: "))

if v1>v2:
    print(v1, " es mayor que ", v2)
elif v2>v1:
    print(v2, " es mayor que ", v1)
else:
    print(v1, " y ", v2, "son iguales")
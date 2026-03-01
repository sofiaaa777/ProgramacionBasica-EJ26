# Problema 25. Ecuación de la recta.

x1 = int (input("Introduce un valor para x en P: "))
y1 = int (input("Introduce un valor para y en P: "))
x2 = int (input ("Introduce un valor para x en Q: "))
y2 = int (input ("Introduce un valor para y en Q: "))

m = int ((y2 - y1) / (x2 - x1))
b = int (m * x2 + y2)


print ("La pendiente de la recta es: ", m)
print ("La ecuación de la recta es: y = ", m, "x +", b)
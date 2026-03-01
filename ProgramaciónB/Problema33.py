# Problema 33. Evaluación del vendedor según volumen de ventas.

nom = input("Introduzca nombre del vendedor: ")
vent = float(input("Introduzca su volumen de ventas en pesos: $"))

if vent < 1000:
    print("Vendedor", nom, "despedido.")
elif vent >= 1000 and vent <= 4999.99:
    print("Vendedor", nom, "en periodo de prueba.")
elif vent >= 5000 and vent <= 9999.99:
    print("Vendedor", nom, "recibe bono del 5%.")
else: print("Vendedor", nom, "recibe bono del 10%.")
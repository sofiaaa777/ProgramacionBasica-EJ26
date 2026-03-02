# Problema 54. Ahorradores.

ahorradores = []
ahorros = []
while True:
    nom = input("Nombre del ahorrador(escribir 'fin' para cancelar): ")
    if nom.lower() == "fin":
        break
    else:
        ahorradores.append(nom)
    ahorro = float(input("Cantidad ahorrada: $"))
    if ahorro >= 0:
        ahorros.append(ahorro)
    else:
        print("Valor inválido")
for i in range(len(ahorradores)):
    if ahorros[i] < 1000:
        ahorros[i] = "no tendrás para tu futuro."
    elif ahorros[i] > 1000000:
        ahorros[i] = "ya merito te retiras"
    else:
        ahorros[i] = ("sigue ahorrando.")
    print (f"Ahorrador {ahorradores[i]} {ahorros[i]}")
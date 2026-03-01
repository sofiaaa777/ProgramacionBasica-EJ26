# Problema 17. Cálculo de beneficio

prec = float (input("Precio por pieza: $"))
cant = int (input ("Cantidad de piezas vendidas: "))
costf = float (input("Costo fijo: $"))
costv = float (input ("Costo variable por pieza: $"))
ing = prec * cant
costot = costv * cant + costf
beneficio = ing - costot
print ("El beneficio total es: $", beneficio)
# Problema 24. Interés simple y compuesto.

cap = float (input("Introduzca el capital inicial: $"))
tasint = float (input("Introduzca la tasa de interés anual: %"))
per = int (input("Introduzca el total de periodos: "))

tasint = tasint / 100
capsim = cap + (cap * tasint * per)
capcom = cap * ((1 + tasint)** per)
print ("Capital simple: ", capsim)
print ("Capital compuesto: ", capcom)
# Problema 31. Evaluación académica.

calif = float(input("Ingrese su calificación: "))
if calif < 0 or calif > 10:
    print("Valor invalido (0-10)")
elif calif < 6:
    print ("Situación académica irregular")
elif calif >= 6 and calif <= 9.9:
    print("Situación académica regular")
else: print("Situación académica excelente")

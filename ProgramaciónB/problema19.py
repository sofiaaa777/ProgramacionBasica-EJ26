# Problema 19. Promedio y datos del alumno.

nom = input ("Introduce tu nombre: ")
bol = int ( input("Introduce tu número de boleta: "))
cal1 = int (input ("Introduce tu 1er calificación: "))
cal2 = int (input ("Introduce tu 2da calificación: "))
cal3 = int (input ("Introduce tu 3ra calificación: "))
cal4 = int (input ("Introduce tu 4ta calificación: "))
cal5 = int (input ("Introduce tu 5ta calificación: "))

prom = (cal1+cal2+cal3+cal4+cal5) /5
print ("Estudiante: ", nom)
print ("Boleta: ", bol)
print ("Promedio: ", prom)
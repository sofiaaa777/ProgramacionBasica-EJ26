# Problema 66. Lista de reprobados.

nombres = []
califs = []

while True:
    nom = input("Introduce el nombre de un alumno (escribe 'no' para cancelar): ")
    if nom.lower() == "no":
        break
    else:
        calif = float(input("Introduce su calificación: "))
        califs.append(calif)
        nombres.append(nom)

def reprobados(califs, nombres):
    alumnos = dict(zip(nombres, califs))
    reprobados = { nom: calif
                   for nom in alumnos.items() if calif <70
                   }
    nombres = []
    for nom in reprobados:
        nombres.append(nom)
    return nombres

lista_reprob = reprobados(califs, nombres)
print ("Lista de reprobados", lista_reprob)

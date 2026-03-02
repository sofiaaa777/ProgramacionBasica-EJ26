# Problema 47. Calificación promedio por materia.

materias = {}
while True:
    mate = input("Introduce una materia (escribe 'fin' para terminar): ")
    if mate.lower() == "fin":
        break
    calificaciones = []

    while True:
        calif = (input("Introduce una calificiación para la materia (escribe 'fin' para terminar): "))
        if calif.lower() == "fin":
            break
        calificaciones.append(float(calif))
    materias[mate] = calificaciones
    for materias, calif in materias.items():
        promedio = sum(calificaciones) / len (calificaciones)
        print(f"{mate} Promedio: {promedio: .2f}")
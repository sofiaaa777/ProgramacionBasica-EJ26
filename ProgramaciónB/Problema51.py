# Problema 51. Asistencia trabajadores.

trabajadores = []
asistencia = []
while True:
    nom = input("Nombre del trabajador (escriba 'fin' para dejar de introducir): ")
    if nom.lower() == "fin":
        break
    else:
        trabajadores.append(nom)
    asist = int(input("Asistencia (0. Falta // 1. Asistencia): "))
    if asist == 0 or asist == 1:
        asistencia.append(asist)
    else:
        print("Opción inválida")
for i in range(len(trabajadores)):
    if asistencia[i] == 0:
        asistencia [i] = "no asistió a trabajar."
    else:
        asistencia[i] = "asistió a trabajar"
    print (f"Trabajador {trabajadores[i]} {asistencia[i]}")
# Problema 62. Calificación final.

def final(calf1, calif2, calif3):
    return (calif1 + calif2+ calif3) / 3

calif1 = float(input("Introduce tu primera calificación: "))
calif2 = float(input("Introduce tu segunda calificación: "))
calif3 = float(input("Introduce tu tercera calificación: "))

print("Calificación final: ", final(calif1, calif2, calif3))
if final(calif1, calif2, calif3) < 70:
    print("Te vas a extra")

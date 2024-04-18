# Generar Datos
import random

def mejor_caso():
    f = open("mejor_caso.dat", "a")
    for n in range(1, 100001):
        f.write(f"{n}\n")
    f.close()

def peor_caso():
    f = open("peor_caso.dat", "a")
    for n in range(100000,0, -1):
        f.write(f"{n}\n")
    f.close()

def caso_promedio():
    f = open("promedio_caso.dat", "a")
    for n in range(1, 100001):
        numero = random.randint(1, 100001)
        f.write(f"{numero}\n")
    f.close()

mejor_caso()
peor_caso()
caso_promedio()
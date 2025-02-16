# Se dan los límites de los rangos. producir números aleatorios dentro de los límites especificados.

from random import randint, random

print("Generar números aleatorios dentro de los límites especificados")
print("---------------------------------------------------------------")
imin = int(input("Introduce el límite inferior: "))
imax = int(input("Introduce el límite superior: "))

print("Número aleatorio entre {} y {}: {}".format(imin, imax, randint(imin, imax)))

fmin = float(input("Introduce el límite inferior: "))
fmax = float(input("Introduce el límite superior: "))

print("Número aleatorio entre {} y {}: {}".format(fmin, fmax, random() * (fmax - fmin) + fmin))

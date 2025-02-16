# A partir del radio de la órbita del planeta y su velocidad orbital, calcule el número de días por año en este planeta.

from math import pi

r = input("Ingrese el radio de la órbita del planeta en km: ")
v = input("Ingrese la velocidad orbital del planeta en km/h: ")
r = float(r)
v = float(v)

# Calculamos el perímetro de la órbita
r = r * 1000000

year = 2 * pi * r / v

year = year / (60 * 60 * 24)

print("El número de días por año en este planeta es: ", round(year))
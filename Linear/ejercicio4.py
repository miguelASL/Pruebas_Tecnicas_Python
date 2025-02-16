# Se ingresan la altura del cilindro y el radio de su base. calcular la superficie total del cilindro

from math import pi

height = float(input("Ingrese la altura del cilindro en cm: "))
radio = float(input("Ingrese el radio de la base del cilindro en cm: "))

circle = pi * radio**2
side = 2 * pi * radio * height
total_area = 2 * circle + side

print("La superficie total del cilindro es: ", total_area, "cm^2")

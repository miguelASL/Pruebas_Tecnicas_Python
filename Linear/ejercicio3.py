# Las longitudes de dos catetos de un triángulo anular se ingresan desde el teclado. calcular su área y perímetro

import math

AB = input("Ingrese la longitud del cateto AB: ")
AC = input("Ingrese la longitud del cateto AC: ")

AB = float(AB)
AC = float(AC)

BC = math.sqrt(AB**2 + AC**2)

superficie = (AB * AC) / 2
perimetro = AB + AC + BC

print("El área del triángulo es: ", superficie)
print("El perímetro del triángulo es: ", perimetro)
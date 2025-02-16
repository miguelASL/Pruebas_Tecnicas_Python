# Introduce el radio. Encuentra la circunferencia y el área correspondientes del círculo.

import math

radio = float(input("Introduce el radio del círculo en cm: "))

circunferencia = 2 * math.pi * radio
area = math.pi * radio**2

print("La circunferencia del círculo es: ", circunferencia, "cm")
print("El área del círculo es: ", area, "cm^2")

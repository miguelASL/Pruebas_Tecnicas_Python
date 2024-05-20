"""
Simula el juego de adivinar un número
"""

import random

ordenador = random.randint(1, 100)
intentos = 0

while True:
    usuario = int(input("Introduce un número: "))
    intentos += 1
    if usuario < ordenador:
        print("El número es mayor")
    elif usuario > ordenador:
        print("El número es menor")
    else:
        print("¡Has acertado!")
        print(f"Has necesitado {intentos} intentos")
        break
    
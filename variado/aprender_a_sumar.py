"""
Haz un programa para aprender a sunmar en poco tiempo
"""

import time
import random

acierto = 0

tiempo_inicio = time.time()

for i in range(5):
    numero_1 = random.randint(1, 10)
    numero_2 = random.randint(1, 10)
    correcto = numero_1 + numero_2
    
    respuesta = int(input(f"cuánto es {numero_1} + {numero_2}? "))
    if respuesta == correcto:
        print("Correcto!")
        acierto += 1
    else:
        print(f"Incorrecto. La respuesta es {correcto}")
        
tiempo_final = time.time()
print(f" has tardado {tiempo_final - tiempo_inicio} segundos")
print(f"Has acertado {acierto} veces")
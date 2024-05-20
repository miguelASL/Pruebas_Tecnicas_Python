"""
Simula erl juego de cara o cruz
"""
import random
opciones = ["cara", "cruz"]
usuario = input("Elige cara o cruz: ").lower()

if usuario not in opciones:
    print("Opción no válida")
    quit()
else:
    maquina = random.choice(opciones)
    print(f"La máquina ha elegido {maquina}")
    
    if usuario == maquina:
        print("Has ganado!")
    else:
        print("Has perdido")
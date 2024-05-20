"""
Haz una funcion que pida una frase y cuente cuantas palabras tiene
"""

def contar():
    frase = input("Escribe una frase: ")
    palabras = frase.split()
    return len(palabras)

print(contar()) 
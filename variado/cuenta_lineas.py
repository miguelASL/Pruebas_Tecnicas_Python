"""
Haz una funcion que cuente las palabras de un archivo de texto
"""

def cuenta_lineas(archivo):
    with open(archivo, 'r') as f:
        data = f.read()
        return len(data.split())

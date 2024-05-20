"""
Haz una funcion que devuelva la diferencia máxima entre dos números de una lista
"""

def diferencia_maxima(lista):
    if len(lista) == 0:
        return 0
    lista.sort()
    min = lista[0]
    max = lista[-1]
    return max - min
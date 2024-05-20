"""
Haz una función que sume los primeros 'n' números utilizados recursividad
"""

def sumar_recusiva(n):
    if n == 0:
        return 0
    else:
        return n + sumar_recusiva(n - 1)
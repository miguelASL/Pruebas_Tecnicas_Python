"""
Haz una funcion que devuelva el factorial de un número
"""

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

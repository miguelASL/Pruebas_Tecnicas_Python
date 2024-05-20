"""
Funcion que devuelva el numero de la sucecion de fibonacci en la posicion n
"""

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fibo = [0, 1]
    for i in range(2, n):
        fibo.append(fibo[-1] + fibo[-2])
    return fibo[-1]

print(fibonacci(10))
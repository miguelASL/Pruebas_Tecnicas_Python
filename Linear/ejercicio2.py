# Escribir un programa que genere un número aleatorio de tres dígitos y calcule la suma de sus dígitos

from random import randint

num = randint(100, 999)
print("Número aleatorio de tres dígitos: ", num)

a = num // 100
b = num // 10 % 10
c = num % 10

suma = a + b + c

print("La suma de los dígitos del número es: ", suma)

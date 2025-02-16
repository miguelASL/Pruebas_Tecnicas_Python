# Se da una pequeña letra en inglés. determinar su número ordinal en el alfabeto

letra = input("Introduce una letra en minúscula: ")
number = ord(letra) - ord("a") + 1

print("El número ordinal de la letra {} es: {}".format(letra, number))

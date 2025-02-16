# Se ingresa un par de números binarios. realice operaciones bit a bit "AND" "OR" "EXCLUSIVE OR" en ellos. mostrar el resultado en la pantalla.

bin1 = input("Introduce el primer número binario: ")
bin2 = input("Introduce el segundo número binario: ")

num1 = int(bin1, 2)
num2 = int(bin2, 2)

print("Operaciones bit a bit en {} y {}".format(bin1, bin2))
print("-------------------------------------------------")
print("AND: {}".format(bin(num1 & num2)[2:]))
print("OR: {}".format(bin(num1 | num2)[2:]))
print("EXCLUSIVE OR: {}".format(bin(num1 ^ num2)[2:]))

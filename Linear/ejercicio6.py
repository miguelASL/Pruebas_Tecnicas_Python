# Se introducen las coordenadas de dos puntos. mostrar la ecuación de la recta que pasa por estos dos puntos

print("Introduzca las coordenadas de dos puntos:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))

print("Introduzca las coordenadas del segundo punto:")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

print("La ecuación de la recta que pasa por los puntos ({}, {}) y ({}, {}) es:".format(
    x1, y1, x2, y2))
k = (y2 - y1) / (x2 - x1)
b = y1 - k * x1
print("y = {}x + {}".format(k, b))

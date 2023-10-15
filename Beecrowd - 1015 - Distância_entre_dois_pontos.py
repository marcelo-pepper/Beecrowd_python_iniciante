from math import sqrt
ponto_1 = input().split(" ")
ponto_2 = input().split(" ")
x1, y1 = ponto_1
x2, y2 = ponto_2
distancia = ((float(x2) - float(x1)) ** 2) + ((float(y2) - float(y1)) ** 2)
result = sqrt(distancia)
print('{:.4f}'.format(result))

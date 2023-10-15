from math import sqrt
num = input().split(" ")
A, B, C = num
A = float(A)
B = float(B)
C = float(C)

delta = B**2 - 4*A*C

if delta < 0.0 or A == 0:
    print('Impossivel calcular')
else:
    x1 = (-B + sqrt(delta)) / (2*A)
    x2 = (-B - sqrt(delta)) / (2*A)
    print('R1 = {:.5f}'.format(x1))
    print('R2 = {:.5f}'.format(x2))

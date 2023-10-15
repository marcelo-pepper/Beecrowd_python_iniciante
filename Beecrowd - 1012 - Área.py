valor = input().split(" ")
A , B, C = valor
area_triangulo = (float(A) * float(C)) / 2 
area_circulo = 3.14159 * float(C) ** 2
area_trapezio = ((float(A) + float(B)) / 2 * float(C))
area_quadrado = float(B) ** 2 
area_retangulo = float(A) * float(B)
print('TRIANGULO: {:.3f}'.format(area_triangulo))
print('CIRCULO: {:.3f}'.format(area_circulo))
print('TRAPEZIO: {:.3f}'.format(area_trapezio))
print('QUADRADO: {:.3f}'.format(area_quadrado))
print('RETANGULO: {:.3f}'.format(area_retangulo))
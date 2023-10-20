num = input().split()
a, b, c = num
a = float(a)
b = float(b)
c = float(c)
list = [a, b, c]
list.sort()
menor = list[0]
medio = list[1]
maior = list[2]
if (a + b) > c and (a + c) > b and (b + c) > a:
    if a == b == c:
        perimetro_equilatero = a * 3
        print('Perimetro = {:.1f}'.format(perimetro_equilatero))
    elif a != b != c:
        perimetro_escaleno = a + b + c
        print('Perimetro = {:.1f}'.format(perimetro_escaleno)) 
    else:
        if maior == medio:
            perimetro_isosceles = (maior + medio)*2
        else:
            perimetro_isosceles = (medio + menor)*2
        print('Perimetro = {:.1f}'.format(perimetro_isosceles))
else:
    area_trapezio = ((a + b)* c) / 2
    print('Area = {:.1f}'.format(area_trapezio))

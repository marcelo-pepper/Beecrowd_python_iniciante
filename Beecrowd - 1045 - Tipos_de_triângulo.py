num = input().split()
l1, l2, l3 = num
l1 = float(l1)
l2 = float(l2)
l3 = float(l3)
list = [l1, l2, l3]
list.sort(reverse=True)
A = list[0]
B = list[1]
C = list[2]
if A >= B + C:
    print('NAO FORMA TRIANGULO')
elif A ** 2 == B ** 2 + C ** 2:
    print('TRIANGULO RETANGULO')
elif A ** 2 > B ** 2 + C ** 2:
    print('TRIANGULO OBTUSANGULO')
elif A ** 2 < B ** 2 + C ** 2:
    print('TRIANGULO ACUTANGULO')
if A == B == C:
    print('TRIANGULO EQUILATERO')
elif A == B or B == C:
    print('TRIANGULO ISOSCELES')

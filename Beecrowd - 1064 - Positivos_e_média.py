valor_1 = float(input())
valor_2 = float(input())
valor_3 = float(input())
valor_4 = float(input())
valor_5 = float(input())
valor_6 = float(input())

soma_positivo = 0
qtd_positivo = 0
if valor_1 > 0:
    qtd_positivo += 1
    soma_positivo += valor_1
if valor_2 > 0:
    qtd_positivo += 1
    soma_positivo += valor_2
if valor_3 > 0:
    qtd_positivo += 1
    soma_positivo += valor_3
if valor_4 > 0:
    qtd_positivo += 1
    soma_positivo += valor_4
if valor_5 > 0:
    qtd_positivo += 1
    soma_positivo += valor_5
if valor_6 > 0:
    qtd_positivo += 1
    soma_positivo += valor_6

media = soma_positivo / qtd_positivo
print('{:.0f} valores positivos'.format(qtd_positivo))
print('{:.1f}'.format(media))

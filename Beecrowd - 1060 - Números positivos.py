valor_1 = float(input())
valor_2 = float(input())
valor_3 = float(input())
valor_4 = float(input())
valor_5 = float(input())
valor_6 = float(input())

qtd_positivo = 0
if valor_1 < 0:
    qtd_positivo += 1
if valor_2 < 0:
    qtd_positivo += 1
if valor_3 < 0:
    qtd_positivo += 1
if valor_4 < 0:
    qtd_positivo += 1
if valor_5 < 0:
    qtd_positivo += 1
if valor_6 < 0:
    qtd_positivo += 1
print('{:.0f} valores positivos'.format(qtd_positivo))

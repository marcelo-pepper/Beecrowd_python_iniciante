valor_1 = float(input())
valor_2 = float(input())
valor_3 = float(input())
valor_4 = float(input())
valor_5 = float(input())
valor_6 = float(input())
valores = [valor_1, valor_2, valor_3, valor_4, valor_5, valor_6]
qtd_positivo = 0
cont = 0
while cont < 6:
    if valores[cont] > 0:
        qtd_positivo += 1
    cont += 1
print('{:.0f} valores positivos'.format(qtd_positivo))

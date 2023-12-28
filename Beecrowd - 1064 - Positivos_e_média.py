valor_1 = float(input())
valor_2 = float(input())
valor_3 = float(input())
valor_4 = float(input())
valor_5 = float(input())
valor_6 = float(input())

valores = [valor_1, valor_2, valor_3, valor_4, valor_5, valor_6]
soma_positivo = 0
qtd_positivo = 0
cont = 0
while cont < 6:
    if valores[cont] > 0:
        qtd_positivo += 1
        soma_positivo += valores[cont]
    cont += 1
media = soma_positivo / qtd_positivo
print('{:.0f} valores positivos'.format(qtd_positivo))
print('{:.1f}'.format(media))

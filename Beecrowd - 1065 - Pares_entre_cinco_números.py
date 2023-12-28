valor_1 = int(input())
valor_2 = int(input())
valor_3 = int(input())
valor_4 = int(input())
valor_5 = int(input())
valores = [valor_1, valor_2, valor_3, valor_4, valor_5]
cont = 0
qtd_par = 0
while cont < 5:
    if valores[cont] % 2 == 0:
        qtd_par += 1
    cont += 1
print('{} valores pares'.format(qtd_par))

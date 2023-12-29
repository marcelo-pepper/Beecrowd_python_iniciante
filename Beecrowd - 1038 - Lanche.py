num = input().split()
cod, qtd = num
cod = int(cod)
qtd = int(qtd)
itens = [4.00, 4.50, 5.00, 2.00, 1.50]

if cod <= 5:
    valor = qtd * itens[cod - 1]
    print('Total: R$ {:.2f}'.format(valor))

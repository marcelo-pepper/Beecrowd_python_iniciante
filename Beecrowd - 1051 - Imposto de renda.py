salario = float(input())

if salario > 0 and salario < 2000.00:
    print('Isento')

elif salario > 2000.01 and salario < 3000.00:
    valor_calculo_8 = salario - 2000
    imposto_8 = (valor_calculo_8 * 8) / 100
    print('R$ {:.2f}'.format(imposto_8))

elif salario > 3000.01 and salario < 4500.00:
    valor_calculo_18 = salario - 3000
    imposto_18 = 80 + ((valor_calculo_18 * 18) / 100)
    print('R$ {:.2f}'.format(imposto_18))

else:
    valor_calculo_28 = salario - 4500
    imposto_28 = 80 + 270 + ((valor_calculo_28 * 28) / 100)
    print('R$ {:.2f}'.format(imposto_28))

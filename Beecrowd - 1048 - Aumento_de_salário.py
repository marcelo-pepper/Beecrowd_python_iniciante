salario = input()
salario = float(salario)
porcentagem = int(0)
if salario <= 0 and salario > 400.00:
    porcentagem += 15
elif salario >= 400.01 and salario <= 800.00:
    porcentagem += 12
elif salario >= 800.01 and salario <= 1200.00:
    porcentagem += 10
elif salario >= 1200.01 and salario <= 2000.00:
    porcentagem += 7
else:
    porcentagem += 4
aumento = (salario * porcentagem) / 100
novo_salario = salario + aumento
print('Novo salario: {:.2f}'.format(novo_salario))
print('Reajuste ganho: {:.2f}'.format(aumento))
print('Em percentual: {} %'.format(porcentagem))

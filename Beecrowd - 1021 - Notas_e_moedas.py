valor_digitado = float(input())
nota100 = valor_digitado // 100
valor_digitado = valor_digitado - nota100 * 100
nota50 = valor_digitado // 50
valor_digitado = valor_digitado - nota50 * 50
nota20 = valor_digitado // 20
valor_digitado = valor_digitado - nota20 * 20
nota10 = valor_digitado // 10
valor_digitado = valor_digitado - nota10 * 10
nota5 = valor_digitado // 5 
valor_digitado = valor_digitado - nota5 * 5
nota2 = valor_digitado // 2 
valor_digitado = valor_digitado - nota2 * 2
moeda_1 = valor_digitado // 1
valor_digitado = valor_digitado - moeda_1 * 1
moeda_50 = valor_digitado // 0.50
valor_digitado = valor_digitado - moeda_50 * 0.50
moeda_25 = valor_digitado // 0.25
valor_digitado = valor_digitado - moeda_25 * 0.25
moeda_10 = valor_digitado // 0.10
valor_digitado = valor_digitado - moeda_10 * 0.10
moeda_5 = valor_digitado // 0.05
valor_digitado = valor_digitado - moeda_5 * 0.05
moeda_01 = valor_digitado // 0.01
valor_digitado = valor_digitado - moeda_01 * 0.01
print('NOTAS:')
print('{:.0f} nota(s) de R$ 100.00'.format(nota100))
print('{:.0f} nota(s) de R$ 50.00'.format(nota50))
print('{:.0f} nota(s) de R$ 20.00'.format(nota20))
print('{:.0f} nota(s) de R$ 10.00'.format(nota10))
print('{:.0f} nota(s) de R$ 5.00'.format(nota5))
print('{:.0f} nota(s) de R$ 2.00'.format(nota2))
print('MOEDAS:')
print('{:.0f} moeda(s) de R$ 1.00'.format(moeda_1))
print('{:.0f} moeda(s) de R$ 0.50'.format(moeda_50))
print('{:.0f} moeda(s) de R$ 0.25'.format(moeda_25))
print('{:.0f} moeda(s) de R$ 0.10'.format(moeda_10))
print('{:.0f} moeda(s) de R$ 0.05'.format(moeda_5))
print('{:.0f} moeda(s) de R$ 0.01'.format(moeda_01))

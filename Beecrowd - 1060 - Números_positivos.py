valores = [float(input()) for _ in range(6)]
qtd_positivo = sum(1 for valor in valores if valor > 0)
print('{:.0f} valores positivos'.format(qtd_positivo))

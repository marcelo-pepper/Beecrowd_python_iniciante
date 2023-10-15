hora = input().split()
hora_inicial, hora_final = hora
hora_inicial = int(hora_inicial)
hora_final = int(hora_final)
if hora_final < hora_inicial:
    duracao = (24 - hora_inicial) + hora_final
else:
    duracao = hora_final - hora_inicial

if duracao < 1:
    duracao += 24
print('O JOGO DUROU {} HORA(S)'.format(duracao))

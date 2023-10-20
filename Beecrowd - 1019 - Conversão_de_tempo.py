tempo = int(input())
tempo_hora = tempo // 3600
tempo = tempo - tempo_hora * 3600
tempo_minuto = tempo // 60
tempo = tempo - tempo_minuto * 60
tempo_segundo = tempo // 1
tempo = tempo - tempo_segundo * 1
print('{}:{}:{}'.format(tempo_hora, tempo_minuto, tempo_segundo))

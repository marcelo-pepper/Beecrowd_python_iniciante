dias = int(input())

ano = dias // 365
dias = dias - ano * 365 

mes = dias // 30
dias = dias - mes * 30

dia = dias // 1
dias = dias - dia * 1

print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dia))
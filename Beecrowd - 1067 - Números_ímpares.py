x = int(input())
if x >= 1 and x <= 1000:
    aux = 1
    while aux <= x:
        numero = aux % 2
        if numero != 0:
            print('{}'.format(aux))
        aux += 1

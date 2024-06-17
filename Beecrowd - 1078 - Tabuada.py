valor = int(input('Digite um valor: '))

if valor > 2 and valor < 1000:
    var_aux = 1
    while var_aux < 11:
        print('{} x {} = {}'.format(var_aux, valor, (var_aux * valor)))
        var_aux += 1

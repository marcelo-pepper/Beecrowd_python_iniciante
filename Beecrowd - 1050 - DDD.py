numero = int(input())
lista_cidade = ["Sao Paulo", "Campinas", "Rio de Janeiro",
                "Vitoria", "Belo Horizonte", "Juiz de Fora", "Brasilia", "Salvador"]
lista_ddd = [11, 19, 21, 27, 31, 32, 61, 71]

if numero in lista_ddd:
    indice = lista_ddd.index(numero)
    print(lista_cidade[indice])
else:
    print('DDD nao cadastrado')

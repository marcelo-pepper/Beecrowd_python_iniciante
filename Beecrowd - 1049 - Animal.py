nome1 = str(input()).strip().upper()
nome2 = str(input()).strip().upper()
nome3 = str(input()).strip().upper()

if nome1 == 'VERTEBRADO':
    if nome2 == 'AVE':
        if nome3 == 'CARNIVORO':
            print('aguia')
        elif nome3 == 'ONIVORO':
            print('pomba')
    elif nome2 == 'MAMIFERO':
        if nome3 == 'ONIVORO':
            print('homem')
        elif nome3 == 'HERBIVORO':
            print('vaca')
elif nome1 == 'INVERTEBRADO':
    if nome2 == 'INSETO':
        if nome3 == 'HEMATOFAGO':
            print('pulga')
        elif nome3 == 'HERBIVORO':
            print('lagarta')
    elif nome2 == 'ANELIDEO':
        if nome3 == 'HEMATOFAGO':
            print('sanguessuga')
        elif nome3 == 'ONIVORO':
            print('minhoca')

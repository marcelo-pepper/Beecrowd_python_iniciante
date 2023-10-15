nota = input().split()
n1, n2, n3, n4 = nota
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

nota_exame = 0.0
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
print('Media: {:.1f}'.format(media))

if media >= 7 :
    print('Aluno aprovado.')

if (media < 5) :
    print('Aluno reprovado.')

if media >= 5 and media <= 6.9:
    nota_exame = float(input())
    media_final = (nota_exame + media) / 2
    print('Aluno em exame.')
    print('Nota do exame: {:.1f}'.format(nota_exame))
    
    if media_final >= 5:
        print('Aluno aprovado.')
        
    else: 
        print('Aluno reprovado.')
    
    print('Media final: {:.1f}'.format(media_final))        

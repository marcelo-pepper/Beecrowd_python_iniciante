valor = input().split(" ")
A, B, C = valor
num_A = int(A)
num_B = int(B)
num_C = int(C)
if num_A > num_C:
    print('{} eh o maior'.format(num_A))
elif num_B > num_A:
    print('{} eh o maior'.format(num_B))
else:
    print('{} eh o maior'.format(num_C))
    
numero = int(input())
mes = ["January", "February", "March", "April", "May", "June",
       "July", "August", "September", "October", "November", "December"]
if numero <= 12:
    print(mes[numero - 1])

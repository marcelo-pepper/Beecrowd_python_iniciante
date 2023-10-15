num = input().split()
n1, n2, n3 = num
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
list = [n1, n2, n3]
list.sort()
print(f"{list[0]}\n{list[1]}\n{list[2]}")
print(f"\n{n1}\n{n2}\n{n3}")
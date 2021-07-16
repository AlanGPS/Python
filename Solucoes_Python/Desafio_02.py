x = int(input())

total = 10

for i in range (0,total):
    if i == 0:
        dobro = x
        print("N[{}] = {}".format(i, dobro))
    else:
        dobro = x * 2
        x = dobro
        print("N[{}] = {}".format(i, dobro))
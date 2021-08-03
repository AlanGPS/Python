n = int(input())

fib_list = []

a = 1
b = 0

for i in range(n):
    c = a + b
    a = b
    b = c

    fib_list.append(str(a))

    fib_string = ' '.join(fib_list)

print(fib_string)

# ----------------------------------

N = int(input())

N = N + 1

for i in range(1, N):
    k = i % 2
    if k == 0:
        print(i)

# ----------------------------------

N = int(input())
T = input().split()

if N >= 1 and N <= 100:

    for i in range(N):
        T[i] = int(T[i])

    minimo = min(T)

    res = T.index(minimo) + 1

    print(res)
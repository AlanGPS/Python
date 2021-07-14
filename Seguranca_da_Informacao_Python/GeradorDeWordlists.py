import itertools

#resultado = itertools.permutations('abcdef', 5)

string = input("String a ser permutada: ")

resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))


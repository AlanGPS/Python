## Exercício da Aula 06

conjunto = {1, 2, 3, 4}
conjunto.add(5)
conjunto.discard(2)
conjunto.remove(3)
print(conjunto)

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

conjunto_uniao = conjunto1.union(conjunto2)
print('União: {}'.format(conjunto_uniao))
conjunto_interseccao = conjunto1.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))
conjunto_diferenca1 = conjunto1.difference(conjunto2)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca1))
conjunto_diferenca2 = conjunto2.difference(conjunto1)
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))

## Diferença Simétrica
conjunto_dif_simet = conjunto1.symmetric_difference(conjunto2)
print('Diferença Simétrica: {}'.format(conjunto_dif_simet))

## Operações
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset1 = conjunto_b.issubset(conjunto_a)
conjunto_subset2 = conjunto_a.issubset(conjunto_b)
print('B é um subconjunto de A? {}'.format(conjunto_subset1))
print('A é um subconjunto de B? {}'.format(conjunto_subset2))
conjunto_supset1 = conjunto_b.issuperset(conjunto_a)
conjunto_supset2 = conjunto_a.issuperset(conjunto_b)
print('B é um superconjunto de A? {}'.format(conjunto_supset1))
print('A é um superconjunto de B? {}'.format(conjunto_supset2))

## Conversão
lista = ['cachorro','cachorro','gato','gato','elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)
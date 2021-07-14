## Exercício da Aula 05

## A lista é definida pelas [ ]
# lista = [1, 3, 5, 7]
# lista_animal = ['cachorro','gato','elefante']
# print(lista)
# print(lista_animal[0])


# for x in lista_animal:
#     print(x)


# soma = 0
# for x in lista:
#     print (x)
#     soma += x
# print(soma)


# print(sum(lista)) ## Realiza a soma da lista
# print(max(lista)) ## Busca o valor máximo
# print(min(lista)) ## Busca o valor mínimo


## Adiconar ou remover itens
# if 'lobo' in lista_animal:
#     print('Existe um lobo na lista.')
# else:
#     print('Não existe um lobo na lista. Será incluido.')
#     lista_animal.append('lobo') ## Adiciona a lista (insert)
#     print(lista_animal)
#
# lista_animal.pop(1) ## Retira da lista
# print(lista_animal)
#
# lista_animal.remove('elefante') ## Retira da lista
# print(lista_animal)


## As lsitas podem ser utilizadas em operações
# nova_lista = lista_animal * 3
# print(nova_lista)


## Posicionar em ordem crescente e decrescente
# lista = [10, 3, 15, 7]
# lista_animal = ['cachorro','gato','elefante','lobo','arara']
# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# lista.reverse()
# lista_animal.reverse()
# print(lista)
# print(lista_animal)


# Tuplas: São listas imutáveis definidas por ()
tupla = (10, 3, 15, 7)
lista_animal = ['cachorro','gato','elefante','lobo','arara']
print(tupla)
print(lista_animal)
print(len(tupla))
print(len(lista_animal))

print(type(tupla))

lista_animal = tuple(lista_animal) ## Converter tupla em lista
print(type(lista_animal))
lista_numerica = list(tupla) ## Converter lista em tupla
print(type(lista_numerica))
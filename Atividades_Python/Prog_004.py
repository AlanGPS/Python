## Exercício da Aula 04

## Descrição de um for
# for x in range(101):
#     print(x)



## Determinar se um número é primo ou não
# a = int(input('Entre com um número: '))
#
# div = 0
#
# for x in range(1, a+1):
#      resto = a % x
#      print(x, resto)
#      if resto == 0:
#          #div = div + 1
#          div += 1
#
# if div == 2:
#     print('Número {} é primo.'.format(a))
# else:
#     print('Número {} não é primo.'.format(a))



## Modificação do anterior
# a = int(input('Entre com um range: '))
#
# for num in range (a + 1):
#     div = 0
#     for x in range(1, num + 1):
#          resto = num % x
#          if resto == 0:
#              div += 1
#
#     if div == 2:
#         print(num)



## Utilizando o while
# a = 0
# while a <= 10:
#     print(a)
#     a += 1

nota = int(input('Entre com a nota: '))
while nota >= 10:
    nota = int(input('Nota inválida. Entre com a nota correta: '))
print('Nota adicionada corretamente: {}'.format(nota))
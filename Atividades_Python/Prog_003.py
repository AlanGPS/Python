## Exercício da Aula 03

# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# if a > b and a > c:
#     print('O maior número é {}'.format(a))
# elif b > a and b > c:
#     print('O maior valor é {}'.format(b))
# else:
#     print('O maior valor é {}'.format(c))
#
# print ('Fim do programa!')



# a = int(input('Entre com o 1º valor: '))
# b = int(input('Entre com o 2º valor: '))
#
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or not resto_b > 0:
#     print('Foi digitado um número par!')
# else:
#     print('Nenhum número par foi digitado!')



a = int(input('1º Bimestre: '))
if a > 10 or a < 0:
    a = int(input('Você digitou errado. \nDigite novamente o 1º Bimestre: '))
b = int(input('2º Bimestre: '))
if b > 10 or b < 0:
    b = int(input('Você digitou errado. \nDigite novamente o 2º Bimestre: '))
c = int(input('3º Bimestre: '))
if c > 10 or c < 0:
    c = int(input('Você digitou errado. \nDigite novamente o 3º Bimestre: '))
d = int(input('4º Bimestre: '))
if d > 10 or d < 0:
    d = int(input('Você digitou errado. \nDigite novamente o 4º Bimestre: '))

media = (a + b + c + d) / 4

# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('Media: {}'.format(media))
# else:
#     print('Foi informado alguma nota errada!')

print('\nMedia: {}'.format(media))
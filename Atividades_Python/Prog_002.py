## Exercício da Aula 02

#a = 10
#b = 6

a = int(input('Entre com o primeiro valor:'))
b = int(input('Entre com o segundo valor:'))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(resto)

## Determinando o tipo da variável
#print(type(soma))
## Convertendo de inteiro para string
#soma = str(soma)
## Mostrando que é uma string
#print(type(soma))
## Ou podemos deixar mais complexa a coisa
print('Soma: ' + str (soma))
## Isso se chama concatenação

## Outra forma de fazer isso é usando o format
print('Soma: {}. Subtração {}.'.format(soma,subtracao))

## Com um enter entre as linhas
resultado = ('Soma: {}.'
      '\nSubtração: {}.'
      '\nMultiplicação: {}.'
      '\nDivisão: {}.'
      '\nResto: {}.'.format(soma,
                            subtracao,
                            multiplicacao,
                            divisao,
                            resto))

print (resultado)

## Outra forma de expressar o resultado
resultado = ('Soma: {sum}.'
      '\nSubtração: {sub}.'
      '\nMultiplicação: {mult}.'
      '\nDivisão: {div}.'
      '\nResto: {rest}.'.format(sum=soma,
                            sub=subtracao,
                            mult=multiplicacao,
                            div=divisao,
                            rest=resto))

print (resultado)
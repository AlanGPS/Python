## Exercício da Aula 08 (03)

# Lambda é uma simplificação do código
contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro','gato','elefante']
print(contador_letras(lista_animais))

# Outro exemplo
soma = lambda a, b: a + b
print(soma(5, 10))

# Outro exemplo
calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}

print(type(calculadora))
soma = calculadora['soma']
print('A soma é: {}'.format(soma(10, 5)))
nota = int(input('Digite a nota a ser convertida: '))

if nota == 0:
    print('\nA nota do aluno é: E')
elif 1 <= nota <= 35:
    print('\nA nota do aluno é: D')
elif 36 <= nota <= 60:
    print('\nA nota do aluno é: C')
elif 61 <= nota <= 85:
    print('\nA nota do aluno é: B')
elif 86 <= nota <= 100:
    print('\nA nota do aluno é: A')
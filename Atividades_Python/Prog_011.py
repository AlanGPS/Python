## Exercício da Aula 11 (01)

# https://docs.python.org/3/library/exceptions.html#exception-hierarchy
# Seguir a hierarquia de erros

# Classe de execessões
lista = [1, 10]
try:
    divisao = 10 / 2
    numero = lista[1]
    # x = a
    arquivo = open('teste.txt', 'r')
except ZeroDivisionError:
    print('Não é possível realizar a divisão!')
# except:
#     print('Erro desconhecido!')
except IndexError:
    print('Erro ao acessar um indice inválido da lista!')
except BaseException as ex:
    print('Erro desocnhecido.\nErro: {}'.format(ex))
else:
    print('Executa quando não houver exceção.')
finally:
    print('\nSempre executa essa parte...')
    print('Fechando o arquivo.')
    arquivo.close()
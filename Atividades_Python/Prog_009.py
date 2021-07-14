## Exercício da Aula 09

## Trabalhando com arquivos
# arquivo = open('teste.txt', 'a') # a = atualiza o arquivo
# arquivo = open('teste.txt', 'w') # w = substitui o arquivo

# diretorio = 'C:/Users/Alan Gonçalves/Documents/teste.txt'
# arquivo = open(diretorio, 'w')
# arquivo.write('Minha primeira escrita!')
# arquivo.close()

def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
    # escrever_arquivo('Primeira linha.\n')
    # atualizar_arquivo('Segunda linha.\n')
    ler_arquivo('teste.txt')



## Leitura e Escrita

# def escrever_arquivo(texto):
#     arquivo = open('teste.txt', 'w')
#     arquivo.write(texto)
#     arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

# def ler_arquivo(nome_arquivo):
#     arquivo = open(nome_arquivo, 'r')
#     texto = arquivo.read()
#     print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas])/4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

if __name__ == '__main__':
    lista_media = media_notas('notas.txt')
    print(lista_media)
    # escrever_arquivo('Primeira linha.\n')
    # aluno = '\nCesar,7,9,8,3'
    # atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('teste.txt')



## Copia e Move

def copia_arquivo(nome_arquivo):
    
    import shutil
    shutil.copy(nome_arquivo,
                'C:/Users/Alan Gonçalves/Documents/')

def move_arquivo(nome_arquivo):
    import shutil
    shutil.move(nome_arquivo,
                'C:/Users/Alan Gonçalves/Documents/')

if __name__ == '__main__':
    copia_arquivo('notas.txt')
    move_arquivo('notas.txt')
## Exercício da Aula 08 (02)

def Contador_Letras(lista_palavras):
    contador = []

    for x in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

if __name__ == '__main__':
    lista = ['cachorro','gato']
    print(contador_letras(lista))
## Exercício da Aula 12

import requests

def retona_dados_cep(cep):
    response = requests.\
        get('https://viacep.com.br/ws/{}/json/'.
        format(cep))
    print(response.status_code)
    print(response.text)
    print(response.json())
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    return dados_cep

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    retona_dados_cep('58040760')
    # response = retorna_response('https://www.alphamaquinasindustriais.com.br/')
    # print(response)
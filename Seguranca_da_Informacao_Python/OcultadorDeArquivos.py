import ctypes

#pasta = input("Digite o caminho da pasta a ser ocultada")

atributo_ocultar = 0x01 ##0x01: Desoculta | 0x02: Oculta

retorno = ctypes.windll.kernel32.SetFileAttributesW('Oculto.txt', atributo_ocultar)
##Pasta no lugar de 'Oculto.txt'

if retorno:
    print("O arquivo foi ocultado.")
else:
    print("O arquivo não foi ocultado.")
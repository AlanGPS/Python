## Exercício da Aula 08 (01)

## Módulos e Funções Anônimas (Lambda)
## São os arquivos que estão dentro da pasta "Exercicios"
## No Python Console: import Prog_001
# From Prog_001 import Televisao

from Prog_007_Tele import Televisao
televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)

from Prog_007_Calc_1 import Calculadora
calculadora = Calculadora(5, 10)
print(calculadora.soma())

from Prog_008_Count import Contador_Letras
lista = ['cachorro','coelho','gato','lebre','elefante']
print(Contador_Letras(lista))
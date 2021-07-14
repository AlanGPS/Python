## Exercício da Aula 07 (03)

# Liga e desliga a TV
class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada == True:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

# televisao = Televisao()
# print('Televisão está ligada? {}'.format(televisao.ligada))
# televisao.power()
# print('Televisão está ligada? {}'.format(televisao.ligada))
# televisao.power()
# print('Televisão está ligada? {}'.format(televisao.ligada))
#
# print('Canal: {}'.format(televisao.canal))
# televisao.power()
# print('Televisão está ligada? {}'.format(televisao.ligada))
# televisao.aumenta_canal()
# televisao.aumenta_canal()
# print('Canal: {}'.format(televisao.canal))
# televisao.diminui_canal()
# print('Canal: {}'.format(televisao.canal))

## Da aula 08 - Chamar apenas pelo nome (main)
if __name__ == '__main__':

    televisao = Televisao()
    print('Televisão está ligada? {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada? {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada? {}'.format(televisao.ligada))

    print('Canal: {}'.format(televisao.canal))
    televisao.power()
    print('Televisão está ligada? {}'.format(televisao.ligada))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.diminui_canal()
    print('Canal: {}'.format(televisao.canal))
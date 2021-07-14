from threading import Thread

"""def carro1(velocidade):
    trajeto = 0
    while trajeto <= 100:
        print('Carro1: ', trajeto)
        trajeto += velocidade

def carro2(velocidade):
    trajeto = 0
    while trajeto <= 100:
        print('Carro2: ', trajeto)
        trajeto += velocidade

#carro1 (10)
#carro2 (20)

t_carro1 = Thread(target = carro1, args = [1])
t_carro2 = Thread(target = carro2, args = [2])"""

# --------------------------------------------
import time

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(1)
        print('Piloto: {} Km {} \n'.format(piloto, trajeto))

t_carro1 = Thread(target = carro, args = [5, 'Alan'])
t_carro2 = Thread(target = carro, args = [4, 'Concorrente'])

t_carro1.start()
t_carro2.start()
import random
import string

#tamanho = 16
tamanho = int(input("Digite a quantidade de caracteres desejado para a senha:"))

chars = string.ascii_letters + string.digits + 'ç!@#$%&-=+'

rnd = random.SystemRandom() ##os.urandom

print("A senha de {} caracteres gerada é: ".format(tamanho))
print(''.join(rnd.choice(chars) for i in range(tamanho)))
from random import randint
from time import sleep
print('vou pensar numero entre 0 e 5 tente adivinhar') # faz o computador pensar
print('-=-' *20)
computador = randint(0,5)
print('-=-' *20)
jogador = int(input('Em qual numeoro eu pensei?'))
print('processando..')
sleep(2)
if jogador == computador:
    print('Parabens vc conseguiu me vencer')
else:
    print('Ganhei eu pensei no numero {:.1f} e não no numero {}'.format(computador, jogador))














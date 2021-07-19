from random import randint
from time import sleep
print('-=--=-'*10)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=--=-'*10)
computador = randint(0, 5)
jogador = int(input('Em que numero pensei? '))
print('PROCESSANDO...')
sleep(1)
if jogador == computador:
    print('Parabéns, voce acertou!!')
else:
    print('Voce errou :/')
print('Eu pensei no número {}!'.format(computador))

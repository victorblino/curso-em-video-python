#Desafio058

from random import randint
from time import sleep

print('-- JOGO DA ADIVINHAÇÃO --\n')
print('Estou pensando em um número de 0 a 10...')
sleep(3)
escolhido = randint(0,10)
print('Pensei!')

acertou = False
palpite = 0

while not acertou:
    n = int(input('Dê um palpite: '))
    palpite += 1
    if escolhido == n:
        acertou = True
    else:
        if escolhido > n:
            print('O número é maior...')
        if escolhido < n:
            print('O número é menor...')

print(f'Parabéns, você acertou! O número correto era: {escolhido}. Você acertou com {palpite} palpites.')
#Desafio028

from random import randint
from time import sleep

n = int(input('Digite um número de 1 a 5 e tente adivinhar oque o computador pensou! '))

escolhido = randint(1, 5)

if n == escolhido:
    print('Hmm...')
    sleep(3)
    print('Parabéns! Você acertou!')
else: 
    print('Hmm...')
    sleep(3)
    print(f'Que pena! Você errou, o número correto era o {escolhido}, tente novamente.')

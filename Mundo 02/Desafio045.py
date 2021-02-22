#Desafio 045

from random import choice
from time import sleep

print('Jokenpo!')

pessoa = int(input("""Escolha uma opção: 
[1] Pedra
[2] Papel
[3] Tesoura
Opção: 
"""))

print('Pedra!')
sleep(1)

print('Papel!')
sleep(1)

print('Tesoura!')
sleep(1)


lista = ['Pedra', 'Papel' , 'Tesoura']

pc = choice(lista)

print(f'Escolha do computador: {pc}')


if pc == 'Pedra':
    if pessoa == 1:
        print('Escolha do usuário: Pedra')
        print('Empate!')
    elif pessoa == 2:
        print('Escolha do usuário: Papel')
        print('O usuário ganhou!')
    elif pessoa == 3:
        print('Escolha do usuário: Tesoura')
        print('O computador ganhou!')
elif pc == 'Papel':
    if pessoa == 1:
        print('Escolha do usuário: Pedra')
        print('O computador ganhou!')
    elif pessoa == 2:
        print('Escolha do usuário: Papel')
        print('Empate!')
    elif pessoa == 3:
        print('Escolha do usuário: Tesoura')
        print('O usuário ganhou!')
elif pc == 'Tesoura':
    if pessoa == 1:
        print('Escolha do usuário: Pedra')
        print('O usuário ganhou!')
    elif pessoa == 2:
        print('Escolha do usuário: Papel')
        print('O computador ganhou!')
    elif pessoa == 3:
        print('Escolha do usuário: Tesoura')
        print('Empate!')
else:
    print('Opção inválida! Tente novamente.')



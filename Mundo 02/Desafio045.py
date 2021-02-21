#Desafio 045

from random import choice

print('Jokenpo!')

pessoa = int(input("""Escolha uma opção: 
[1] Pedra
[2] Papel
[3] Tesoura
Opção: 
"""))

lista = ['pedra', 'papel' , 'tesoura']

pc = choice(lista)


#computador ganha
if pessoa == 1 and pc == 'papel':
    print(f'O computador ganhou! Ele escolheu {pc}!')
elif pessoa == 2 and pc == 'tesoura':
    print(f'O computador venceu! Ele escolheu {pc}!')
elif pessoa == 3 and pc == 'pedra':
    print(f'O computador venceu! Ele escolheu {pc}!')
#pessoa ganha
elif pessoa == 2 and pc == 'pedra':
    print(f'Parabéns, você ganhou! O computador escolheu {pc}!')
elif pessoa == 3 and pc == 'papel':
    print(f'Parabéns, você venceu! O computador escolheu {pc}!')
elif pessoa == 1 and pc == 'tesoura':
    print(f'Parabéns você venceu! O computador escolheu {pc}!')
else:
    print('Empate! Nenhum dos dois venceram!')


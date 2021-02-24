#Desafio052

import colorsys

n = int(input('Insira um número:'))
tot = 0


for c in range (1, n + 1):
    if n % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[m', end='')
print(f'O número {n} é divisível {tot} vezes.')
if tot == 2:
    print('Então ele é primo!')
else:
    print('Ele não é primo!')
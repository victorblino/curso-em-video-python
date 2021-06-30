#Exercicio075

from random import randint

sorteados = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
cont = 0

print('Os números sorteados foram: ', end='')

for n in sorteados:
    cont+=1
    print(n, end='')
    print(', ' if cont <= 4 else '', end='')
print(f'\nO maior valor é {max(sorteados)} e o menor é {min(sorteados)}.')
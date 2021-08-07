#Exercício091

from random import randint
from time import sleep
from operator import itemgetter

ranking = dict()

jogo = {
    'Jogador 1': randint(1,6),
    'Jogador 2': randint(1,6),
    'Jogador 3': randint(1,6),
    'Jogador 4': randint(1,6)
}

for k, v in jogo.items():
    sleep(1)
    print(f'O {k} tirou {v} no dado.')

print('-' * 20)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com o dado {v[1]}.')




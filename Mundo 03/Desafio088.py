#Exercício088

from random import randint
lista = list()
jogos = list()
njogos = int(input('Quantos jogos você quer que eu sorteie? '))
total = 0 

print('-- GERADOR DA SORTE TELESENA --')
while total < njogos:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break

    jogos.append(lista[:])
    lista.clear()
    total += 1 

for i, l in enumerate(jogos):
    print(f'{i+1}º jogo: {l}')


#Exercício100

from random import randint

def sorteia(nSorteados):
    for cont in range(0,5):
        n = randint(1, 10)
        nSorteados.append(n)
        print(f'{cont+1}º número sorteado: {n}')


def somaPar(nSorteados):
    soma = 0
    for valor in nSorteados:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valores pares da lista {nSorteados} é: {soma}')

numeros = list()
sorteia(numeros)
somaPar(numeros)

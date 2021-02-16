#Desafio020

from random import shuffle

n1 = input('Insira o primeiro aluno: ')
n2 = input('Insira o segundo aluno: ')
n3 = input('Insira o terceiro aluno: ')
n4 = input('Insira o quarto aluno: ')
n5 = input('Insira o quinto aluno: ')

lista = [n1, n2, n3, n4, n5]
shuffle(lista)

print('A ordem dos alunos será: {}.'.format(lista))
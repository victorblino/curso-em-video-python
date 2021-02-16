#Desafio019

from random import choice

n1 = input('Escolha o primeiro aluno: ')
n2 = input('Escolha o segundo aluno: ')
n3 = input('Escolha o terceiro aluno: ')
n4 = input('Escolha o quarto aluno: ')
n5 = input('Escolha o quinto aluno: ')

lista = [n1, n2, n3, n4, n5]
escolhido = choice(lista)

print('\nO aluno escolhido foi: {}'.format(escolhido))
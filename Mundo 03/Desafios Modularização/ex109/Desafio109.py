#Exercício107

import moeda

valor = float(input('Digite o valor: '))
print('-' * 20)
print(f'Valor Inserido: {moeda.moeda(valor)}')
print(f'O dobro de R${moeda.moeda(valor)} é {moeda.dobro(valor, True)}')
print(f'A metade de R${moeda.moeda(valor)} é {moeda.metade(valor, True)}')
print(f'Aumentando 10%, o valor fica no total de {moeda.aumentar(valor, True)}')
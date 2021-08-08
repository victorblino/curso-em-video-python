#Exercício107

import moeda

valor = float(input('Digite o valor: '))
print('-' * 20)
print(f'Valor Inserido: {moeda.moeda(valor)}')
print(f'O dobro de R${moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'A metade de R${moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'Aumentando 10%, o valor fica no total de {moeda.moeda(moeda.dobro(valor))}')
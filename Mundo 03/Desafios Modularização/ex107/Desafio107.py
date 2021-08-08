#Exercício107

import moeda

valor = float(input('Digite o valor: '))
print('-' * 20)
print(f'Valor Inserido: R${valor}')
print(f'O dobro de R${valor} é R${moeda.dobro(valor)}')
print(f'A metade de R${valor} é R${moeda.metade(valor)}')
print(f'Aumentando 10%, o valor fica no total de R${moeda.aumentar(valor, 10)}')

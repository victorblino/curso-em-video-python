#Desafio041

from datetime import date

print('-- Confederação Nacional de Natação --')

ano = float(input('Insira o ano que você nasceu: '))
idade = date.today().year - ano

if idade <= 9:
    print('A categoria para essa idade é MIRIM!')
elif idade <= 14:
    print('A categoria para essa idade é: INFANTIL!')
elif idade <= 19:
    print('A sua categoria para essa idade é: JUNIOR!')
elif idade <= 25:
    print('A categoria para essa idade é: SÊNIOR!')
else:
    print('A categoria para essa idade é: MASTER!')

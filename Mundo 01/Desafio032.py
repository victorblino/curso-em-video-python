#Desafio032

from datetime import date

ano = int(input('Insira um ano: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:

    print(f'O ano de {ano} é bissexto!')

else:
    print(f'O ano de {ano} não é bissexto!')
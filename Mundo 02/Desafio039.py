#Desafio039

from datetime import date
data = date.today().year

ano = int(input('Que ano você nasceu? '))
idade = data - ano
alistamento = idade - 18
if idade == 18:
    print(f'Você precisa fazer o alistamento militar!')
elif idade > 18:
    print(f'Já passou {alistamento} ano(s) de você se alistar!')
else:
    print(f'Você ainda não tem idade para se alistar! Faltam {alistamento} ano(s)')
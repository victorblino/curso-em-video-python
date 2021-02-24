#Desafio054

from datetime import date

maioridade = 0
menor = 0

for c in range(1, 8):
    idade = int(input(f'Insira a data de nascimento da {c}º pessoa: '))
    pessoas = date.today().year - idade
    if pessoas >= 18: #ou 21 anos, eu preferi fazer com 18 :p
        maioridade += 1 
    else:
        menor += 1

print(f'No total, {maioridade} pessoas já atingiram a maioridade. {menor} pessoas, ainda não atingiram.')

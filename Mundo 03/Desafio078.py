#Exercício078

valores = []

maior = 0 
menor = 0 

for valor in range(0, 5):
    valores.append(int(input(f'Insira o {valor+1}º valor: ')))
    if valor == 0:
        menor = maior = valores[valor]
    else: 
        if valores[valor] > maior:
            maior = valores[valor]
        if valores[valor] < menor:
            menor = valores[valor]

print(f'Você digitou os seguintes valores: {valores}')

print(f'O maior número é {maior}. Eu encontrei ele na(s) posição: ', end='')
for pos, num in enumerate(valores):
    if num == maior:
        print(f'{pos+1}... ', end='')

print(f'\nO menor número é {menor}. Eu encontrei ele na(s) posição: ', end='')
for pos, num in enumerate(valores):
    if num == menor:
        print(f'{pos+1}... ', end='')



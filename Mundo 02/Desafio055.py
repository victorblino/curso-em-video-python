#Desafio055

maior = 0
menor = 0

for pessoa in range(1, 5):
    peso = float(input(f'Insira o pessoa da {pessoa}º pessoa: '))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'Maior peso: {maior}\nMenor peso: {menor}')

    
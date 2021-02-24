#Desafio056


print('-'*5)
print('ANALISADOR')
print('-'*5)

velho = 0
idade = 0
soma = 0
nomevelho = ''
totalmulheres = 0

for p in range(1, 5):
 
    print(f'{p}º PESSOA:')
    nome = str(input('Insira o nome da pessoa: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('SEXO [M/F]: ')).lower().strip()
    print('-'*5)

    soma += idade # para a média do grupo

    if p == 1 and sexo in 'Mm':
        velho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > velho:
        velho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulheres += 1


mediaidade = soma/4
print(f'A média da idade do grupo é: {mediaidade} anos. O homem mais velho se chama {nomevelho}. A quantidade de mulheres que tem menos de 20 anos é {totalmulheres}.')

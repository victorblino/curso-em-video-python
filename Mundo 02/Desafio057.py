#Desafio057

sexo = str(input('Digita um sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Sexo inválido! Por favor, digite o seu sexo [M/F]: ')).strip().upper()[0]
print(f'Sexo escolhido: {sexo}')

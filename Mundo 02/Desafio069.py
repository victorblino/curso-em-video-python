#Desafio069

homensCadastrados = Mulheres20 = maiorDezoito = 0

while True:
    print('-- CADASTRO DE PESSOAS --')
    idade = int(input('Insira a idade: '))
    if idade > 18:
        maiorDezoito+=1
    sexo = str(input('Insira o sexo [M/F]: ')).upper()[0]
    if sexo == 'M':
        homensCadastrados+=1
    if sexo == 'F' and idade < 20:
        Mulheres20+=1
    opção = str(input('Quer continuar [S/N]? ')).upper()[0]
    if opção == 'N':
        break
print(f'Dados: {maiorDezoito} pessoas tem mais de 18 anos.\n{homensCadastrados} homens cadastrados.\n{Mulheres20} mulheres com mais de 20 anos. ')
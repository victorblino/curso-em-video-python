#Exercício094

pessoas = dict()
totalPessoas = list()
soma = media = 0

while True:
    pessoas.clear()
    pessoas["nome"] = str(input('Insira o nome: '))
    while True:
        pessoas["sexo"] = str(input('Insira o sexo [M/F]: ')).upper()[0]
        if pessoas["sexo"] in 'MF':
            break
        print('Opção Inválida! Por favor, insira o sexo corretamente. M para Masculino e F para feminino.')

    pessoas["idade"] = int(input('Insira a idade: '))
    soma += pessoas["idade"]
    totalPessoas.append(pessoas.copy())

    while True:
        r = str(input('Quer continuar [S/N]? ')).upper()
        if r in 'SN':
                break
        print('Opção Inválida! Por favor, digite S para SIM e N para NÃO.')
    if r == 'N':
        break

media = soma/len(totalPessoas)

print(f'Ao todo, foram {len(totalPessoas)} foram cadastradas.')
print(f'A média de idade é: {media:.1f} anos')

print(f'Mulheres cadastradas: ', end='')
for p in totalPessoas:
    if p["sexo"] in 'F':
        print(f'{p["nome"]}', end=', ')

print('Pessoas com idade em cima da média: ', end=' ')
for p in totalPessoas:
    print(' ')
    if p["idade"] > media:
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')

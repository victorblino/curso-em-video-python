#Exercício084

pessoas = list()
dados = list()
maior = menor = 0

while True:
    pessoas.append(str(input('Insira o nome da pessoa: ')))
    pessoas.append(int(input('Insira o peso dessa pessoa: ')))
    dados.append(pessoas[:])
    
    if len(dados) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    
    pessoas.clear()

    resposta = str(input('Deseja continuar? [S/N]')).upper()
    if resposta in 'nN':
        break

print(f'As pessoas cadastradas, foram: {dados}')
print(f'Ao todo, você cadastrou {len(dados)} pessoas.')
print(f'O maior peso foi de {maior} KG')
print(f'O menor peso foi de {menor} KG')
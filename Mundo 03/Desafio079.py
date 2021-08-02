#Exercício079

valores = []

while True:
    n = int(input('Insira um valor: '))
    if n not in valores:
        valores.append(n)
    else:
        print('Esse valor já existe! Não irei adicionar :/')

    resp = str(input('Deseja continuar [S/N]? '))
    if resp in 'nN':
        break

valores.sort()
print(f'Aqui estão os valores digitados em ordem crescente: {valores}')
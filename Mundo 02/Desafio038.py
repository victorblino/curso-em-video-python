#Desafio038

n1 = int(input('Insira o primeiro número:'))
n2 = int(input('Insira o segundo número: '))

if n1 == n2:
    print('Não existe número maior, os dois são iguais!')
elif n1 > n2:
    print(f'O número {n1} é maior que o número {n2}')
else:
    print(f'O número {n2} é maior que o número {n1}')


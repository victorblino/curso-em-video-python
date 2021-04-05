#Desafio059
from time import sleep

print('Calculadora:')

n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
resultado = 0

opção = 0

while opção != 5:
    
    print('''Escolha uma opção:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    ''')
    opção = int(input('Opção: '))

    if opção == 1:
        resultado = n1 + n2
        print(f'A soma de {n1} + {n2} é: {resultado}.')
    elif opção == 2:
            resultado = n1 * n2
            print(f'A multiplicação de {n1} x {n2} é: {resultado}.')
    elif opção == 3:
        if n1 > n2:
            print(f'O número {n1} é maior do que {n2}.')
        elif n2 > n1:
            print(f'O número {n2} é maior do que {n1}.')
        else:
            print(f'{n1} e {n2} são iguais!')
    elif opção == 4:
        print('Reiniciando...')
        sleep(1.5)
        n1 = int(input('Insira um novo número: '))
        n2 = int(input('Insira outro número: '))
    print('Opção inválida!')
print('Programa finalizado!')

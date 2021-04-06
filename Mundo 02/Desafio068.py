#Desafio068

from random import randint 

win = defeat = 0

while True:
    pcNúmero = randint(0, 10)
    n = int(input('Escolha um número: '))
    total = pcNúmero + n
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Escolha entre par ou impar [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {n} e o computador {pcNúmero}. A soma é {total}!', end=' ')
    print('DEU PAR!' if total % 2 == 0 else 'DEU IMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            win+=1
        else:
            print('Você perdeu!')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            win+=1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Derrota... Você ganhou {win} vezes.')
            
    

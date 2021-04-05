#Desafio061

print('-- GERADOR DE PA --')

n1 = int(input('Insira o termo: '))
razão = int(input('Insira a razão: '))

termo = n1
cont = 1
total = 0
opção = 10


while opção != 0:
    total = total + opção
    while cont <= total:
        print(f'{termo}', end=' -> ')
        termo += razão
        cont += 1
    print('PAUSA')
    opção = int(input('Quantos termos a mais você quer? R: '))

print(f'Progressão finalizada com {total} termos.')
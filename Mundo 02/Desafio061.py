#Desafio061

print('-- GERADOR DE PA --')

n1 = int(input('Insira o termo: '))
razão = int(input('Insira a razão: '))

termo = n1
cont = 1

while cont <= 10:
    print(f'{termo}', end=' -> ')
    termo += razão
    cont += 1
print('FIM')
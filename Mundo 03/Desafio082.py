#Exercício082

lista = []
pares = []
impares = []

while True:
    n = int(input('Insira um valor: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break

print(f'Os números digitados foram: {lista}')
print(f'Os números parem são: {pares}')
print(f'Os números impares são: {impares}')
#Exercício085

numeros = [[], []]
valor = 0

for n in range(1,8):
    valor = int(input(f'Insira o {n}º número: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

numeros[0].sort()
numeros[1].sort()

print(f'Os números pares são: {numeros[0]}')
print(f'Os números impares são: {numeros[1]}')


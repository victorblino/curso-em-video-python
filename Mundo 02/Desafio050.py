#Desafio050

contador = 0
soma = 0

for c in range(1,7):
    n = int(input('Insira um número:'))
    if n % 2 == 0:
        soma += n
        contador += 1
print(f'A soma de {contador} números pares inseridos é: {soma}')
    
        
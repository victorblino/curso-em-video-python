#Desafio065

escolha = 'S'
soma = quantidade = média = maior = menor = 0

while escolha in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quantidade += 1
    if quantidade == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    escolha = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]

média = soma / quantidade

print(f'O maior número foi {maior}, o menor foi {menor} e a média entre eles é: {média}')
